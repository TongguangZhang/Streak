import sys
import pathlib

from fastapi.encoders import jsonable_encoder
from supabase import AClient, PostgrestAPIResponse

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from models import weekly_goal_models

# ==========================================
# CRUD Handlers for weekly_goal
# ==========================================


async def create_weekly_goal(
    weekly_goal: weekly_goal_models.WeeklyGoal, supabase: AClient
) -> weekly_goal_models.WeeklyGoalInDB:
    res: PostgrestAPIResponse = await supabase.table("weekly_goal").insert(jsonable_encoder(weekly_goal)).execute()
    weekly_goal = weekly_goal_models.WeeklyGoalInDB(**res.data[0])
    return weekly_goal


async def get_weekly_goal(weekly_goal_id: str, supabase: AClient) -> weekly_goal_models.WeeklyGoalInDB:
    res: PostgrestAPIResponse = await supabase.table("weekly_goal").select("*").eq("id", weekly_goal_id).execute()
    weekly_goal = weekly_goal_models.WeeklyGoalInDB(**res.data[0])
    return weekly_goal


async def update_weekly_goal(
    weekly_goal_id: str, weekly_goal_update: weekly_goal_models.OptionalWeeklyGoal, supabase: AClient
) -> weekly_goal_models.WeeklyGoalInDB:
    res: PostgrestAPIResponse = await (
        supabase.table("weekly_goal")
        .update(jsonable_encoder(weekly_goal_update.model_dump(exclude_none=True)))
        .eq("id", weekly_goal_id)
        .execute()
    )
    weekly_goal = weekly_goal_models.WeeklyGoalInDB(**res.data[0])
    return weekly_goal


async def delete_weekly_goal(weekly_goal_id: str, supabase: AClient) -> weekly_goal_models.WeeklyGoalInDB:
    res: PostgrestAPIResponse = await supabase.table("weekly_goal").delete().eq("id", weekly_goal_id).execute()
    weekly_goal = weekly_goal_models.WeeklyGoalInDB(**res.data[0])
    return weekly_goal
