import sys
import pathlib
import datetime

from fastapi.encoders import jsonable_encoder
from supabase import AClient, PostgrestAPIResponse

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from models import goal_models

# ==========================================
# CRUD Handlers for goal
# ==========================================


async def create_goal(goal: goal_models.Goal, supabase: AClient) -> goal_models.GoalInDB:
    res: PostgrestAPIResponse = await supabase.table("goal").insert(jsonable_encoder(goal)).execute()
    goal = goal_models.GoalInDB(**res.data[0])
    return goal


async def get_goal(goal_id: str, supabase: AClient) -> goal_models.GoalInDB:
    res: PostgrestAPIResponse = await supabase.table("goal").select("*").eq("id", goal_id).execute()
    goal = goal_models.GoalInDB(**res.data[0])
    return goal


async def update_goal(goal_id: str, goal_update: goal_models.OptionalGoal, supabase: AClient) -> goal_models.GoalInDB:
    res: PostgrestAPIResponse = await (
        supabase.table("goal")
        .update(jsonable_encoder(goal_update.model_dump(exclude_none=True)))
        .eq("id", goal_id)
        .execute()
    )
    goal = goal_models.GoalInDB(**res.data[0])
    return goal


async def delete_goal(goal_id: str, supabase: AClient) -> goal_models.GoalInDB:
    res: PostgrestAPIResponse = await supabase.table("goal").delete().eq("id", goal_id).execute()
    goal = goal_models.GoalInDB(**res.data[0])
    return goal


# ==========================================
# Business logic for goal
# ==========================================


async def activate_goal(goal_id: str, supabase: AClient) -> goal_models.GoalInDB:
    goal = await get_goal(goal_id, supabase)
    goal.active = True
    goal.history.append(goal_models.GoalHistory(start=datetime.datetime.now(), count=goal.count))
    goal = await update_goal(goal_id, goal, supabase)
    return goal


async def deactivate_goal(goal_id: str, supabase: AClient) -> goal_models.GoalInDB:
    goal = await get_goal(goal_id, supabase)
    goal.active = False
    goal.history[-1].end = datetime.datetime.now()
    goal = await update_goal(goal_id, goal, supabase)
    return goal
