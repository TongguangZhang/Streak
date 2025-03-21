import sys
import pathlib
import datetime

from fastapi.encoders import jsonable_encoder
from supabase import AClient, PostgrestAPIResponse

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from models import weekly_goal_models, goal_models, week_models
from responses import week_admin_responses
from services import week_crud_handler


# ==========================================
# Business logic for weeks
# ==========================================


async def get_weeks(supabase: AClient) -> list[week_admin_responses.WeekData]:
    res = await supabase.table("week").select("*").execute()
    weeks = {week["id"]: week_admin_responses.WeekData(**week) for week in res.data}
    weekly_goals = await supabase.table("weekly_goal").select("*").execute()
    weekly_goals = [weekly_goal_models.WeeklyGoalInDB(**goal) for goal in weekly_goals.data]
    goals = await supabase.table("goal").select("*").execute()
    goals = {goal["id"]: goal_models.GoalInDB(**goal) for goal in goals.data}
    for weekly_goal in weekly_goals:
        week_id = str(weekly_goal.week_id)
        goal_id = str(weekly_goal.goal_id)
        weeks[week_id].total_set += goals[goal_id].count
        weeks[week_id].total_achieved += weekly_goal.progress

    return list(weeks.values())


async def create_new_week(supabase: AClient) -> week_models.WeekInDB:
    week = week_models.Week()
    week_in_db = await week_crud_handler.create_week(week, supabase)

    goals = await supabase.table("goal").select("*").eq("active", True).execute()

    if not goals.data:
        return week_in_db

    weekly_goals = [
        weekly_goal_models.WeeklyGoal(goal_id=goal_models.GoalInDB(**goal).id, week_id=week_in_db.id)
        for goal in goals.data
    ]
    _ = await supabase.table("weekly_goal").insert(jsonable_encoder(weekly_goals)).execute()

    return week_in_db


async def get_latest_week(supabase: AClient) -> week_models.WeekInDB:
    res: PostgrestAPIResponse = (
        await supabase.table("week").select("*").order("start_date", desc=True).limit(1).execute()
    )
    if not res.data:
        raise Exception("No weeks found")

    week = week_models.WeekInDB(**res.data[0])

    today = datetime.date.today()
    if today.weekday() == 0 and today != week.start_date:
        week = await create_new_week(supabase)

    return week


async def get_weekly_goals(week_id: str, supabase: AClient) -> list[weekly_goal_models.WeeklyGoalInDB]:
    res: PostgrestAPIResponse = await supabase.table("weekly_goal").select("*").eq("week_id", week_id).execute()
    weekly_goals = {str(goal["goal_id"]): weekly_goal_models.WeeklyGoalInDB(**goal) for goal in res.data}
    res: PostgrestAPIResponse = await supabase.table("goal").select("*").in_("id", list(weekly_goals.keys())).execute()
    combined_goals = [
        week_admin_responses.CombinedGoal(**{**goal, **weekly_goals[goal["id"]].model_dump()}) for goal in res.data
    ]
    combined_goals.sort(key=lambda x: x.created_at)
    return combined_goals
