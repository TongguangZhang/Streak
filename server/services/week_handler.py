import sys
import pathlib

from fastapi.encoders import jsonable_encoder
from supabase import AClient, PostgrestAPIResponse

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from models import week_models, weekly_goal_models, goal_models

# ==========================================
# CRUD Handlers for week
# ==========================================


async def create_week(week: week_models.Week, supabase: AClient) -> week_models.WeekInDB:
    res: PostgrestAPIResponse = await supabase.table("week").insert(jsonable_encoder(week)).execute()
    week = week_models.WeekInDB(**res.data[0])
    return week


async def get_week(week_id: str, supabase: AClient) -> week_models.WeekInDB:
    res: PostgrestAPIResponse = await supabase.table("week").select("*").eq("id", week_id).execute()
    week = week_models.WeekInDB(**res.data[0])
    return week


async def update_week(week_id: str, week_update: week_models.OptionalWeek, supabase: AClient) -> week_models.WeekInDB:
    res: PostgrestAPIResponse = await (
        supabase.table("week")
        .update(jsonable_encoder(week_update.model_dump(exclude_none=True)))
        .eq("id", week_id)
        .execute()
    )
    week = week_models.WeekInDB(**res.data[0])
    return week


async def delete_week(week_id: str, supabase: AClient) -> week_models.WeekInDB:
    res: PostgrestAPIResponse = await supabase.table("week").delete().eq("id", week_id).execute()
    week = week_models.WeekInDB(**res.data[0])
    return week


# ==========================================
# Business logic for week
# ==========================================


async def create_new_week(supabase: AClient) -> week_models.WeekInDB:
    week = week_models.Week()
    week_in_db = await create_week(week, supabase)

    goals = await supabase.table("goal").select("*").eq("active", True).execute()

    weekly_goals = [
        weekly_goal_models.WeeklyGoal(week_id=week_in_db.id, goal_id=goal_models.GoalInDB(goal).id)
        for goal in goals.data
    ]
    res = await supabase.table("weekly_goal").insert(jsonable_encoder(weekly_goals)).execute()

    return week_in_db


async def check_week_complete(week_id: str, supabase: AClient) -> week_models.WeekInDB:
    week = await get_week(week_id, supabase)
    weekly_goals = await supabase.table("weekly_goal").select("*").eq("week_id", week_id).execute()
    for goal in weekly_goals.data:
        goal_in_db = weekly_goal_models.WeeklyGoalInDB(**goal)
        if not goal_in_db.completed:
            return week
    week.completed = True
    week = await update_week(week_id, week, supabase)
    return week
