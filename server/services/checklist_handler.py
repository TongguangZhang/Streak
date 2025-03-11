import sys
import pathlib
import datetime

from fastapi.encoders import jsonable_encoder
from supabase import AClient, PostgrestAPIResponse

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from models import weekly_goal_models, goal_models, week_models
from responses import checklist_responses
from services import weekly_goal_crud_handler, week_crud_handler


# ==========================================
# Business logic for checklisting
# ==========================================


async def get_latest_week(supabase: AClient) -> week_models.WeekInDB:
    res: PostgrestAPIResponse = (
        await supabase.table("week").select("*").order("start_date", desc=True).limit(1).execute()
    )
    if not res.data:
        raise Exception("No weeks found")

    week = week_models.WeekInDB(**res.data[0])
    return week


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


async def get_weekly_goals(week_id: str, supabase: AClient) -> list[weekly_goal_models.WeeklyGoalInDB]:
    res: PostgrestAPIResponse = await supabase.table("weekly_goal").select("*").eq("week_id", week_id).execute()
    weekly_goals = {str(goal["goal_id"]): weekly_goal_models.WeeklyGoalInDB(**goal) for goal in res.data}
    res: PostgrestAPIResponse = await supabase.table("goal").select("*").in_("id", list(weekly_goals.keys())).execute()
    combined_goals = [
        checklist_responses.CombinedGoal(**{**goal, **weekly_goals[goal["id"]].model_dump()}) for goal in res.data
    ]
    combined_goals.sort(key=lambda x: x.created_at)
    return combined_goals


async def check_weekly_goal(weekly_goal_id: str, supabase: AClient) -> weekly_goal_models.WeeklyGoalInDB:
    weekly_goal = await weekly_goal_crud_handler.get_weekly_goal(weekly_goal_id, supabase)

    weekly_goal.progress += 1
    weekly_goal.check_history.append(datetime.datetime.now())

    weekly_goal = await weekly_goal_crud_handler.update_weekly_goal(weekly_goal_id, weekly_goal, supabase)
    return weekly_goal


async def uncheck_weekly_goal(weekly_goal_id: str, supabase: AClient) -> weekly_goal_models.WeeklyGoalInDB:
    weekly_goal = await weekly_goal_crud_handler.get_weekly_goal(weekly_goal_id, supabase)

    weekly_goal.progress -= 1
    weekly_goal.check_history.pop()

    weekly_goal = await weekly_goal_crud_handler.update_weekly_goal(weekly_goal_id, weekly_goal, supabase)
    return weekly_goal


async def get_last_check(weekly_goal_id: str, supabase: AClient) -> datetime.datetime | None:
    weekly_goal = await weekly_goal_crud_handler.get_weekly_goal(weekly_goal_id, supabase)
    if weekly_goal.check_history:
        return weekly_goal.check_history[-1]
    return None
