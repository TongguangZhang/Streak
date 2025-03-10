import sys
import pathlib

from fastapi import APIRouter, HTTPException

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from config import root_logger
from dependencies import supabase_dep
from models import goal_models
from services import goal_handler


router = APIRouter()

# ==========================================
# CRUD for goal
# ==========================================


@router.post("/")
async def create_goal(goal: goal_models.Goal, supabase: supabase_dep.SupabaseDep) -> goal_models.GoalInDB:
    try:
        res = await goal_handler.create_goal(goal, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{goal_id}")
async def get_goal(goal_id, supabase: supabase_dep.SupabaseDep) -> goal_models.GoalInDB:
    try:
        res = await goal_handler.get_goal(goal_id, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{goal_id}")
async def update_goal(
    goal_id: str,
    goal: goal_models.OptionalGoal,
    supabase: supabase_dep.SupabaseDep,
) -> goal_models.GoalInDB:
    try:
        res = await goal_handler.update_goal(goal_id, goal, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{goal_id}")
async def delete_goal(goal_id: str, supabase: supabase_dep.SupabaseDep) -> goal_models.GoalInDB:
    try:
        res = await goal_handler.delete_goal(goal_id, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


# ==========================================
# Business logic for goal
# ==========================================


@router.patch("/{goal_id}/activate")
async def activate_goal(goal_id: str, supabase: supabase_dep.SupabaseDep) -> tuple[bool, goal_models.GoalInDB]:
    try:
        res = await goal_handler.activate_goal(goal_id, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{goal_id}/deactivate")
async def deactivate_goal(goal_id: str, supabase: supabase_dep.SupabaseDep) -> tuple[bool, goal_models.GoalInDB]:
    try:
        res = await goal_handler.deactivate_goal(goal_id, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))
