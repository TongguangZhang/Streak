import sys
import pathlib

from fastapi import APIRouter, HTTPException

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from config import root_logger
from dependencies import supabase_dep
from models import weekly_goal_models
from services import weekly_goal_crud_handler


router = APIRouter()

# ==========================================
# CRUD for weekly_goal
# ==========================================


@router.post("/")
async def create_weekly_goal(
    weekly_goal: weekly_goal_models.WeeklyGoal, supabase: supabase_dep.SupabaseDep
) -> weekly_goal_models.WeeklyGoalInDB:
    try:
        res = await weekly_goal_crud_handler.create_weekly_goal(weekly_goal, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{weekly_goal_id}")
async def get_weekly_goal(weekly_goal_id, supabase: supabase_dep.SupabaseDep) -> weekly_goal_models.WeeklyGoalInDB:
    try:
        res = await weekly_goal_crud_handler.get_weekly_goal(weekly_goal_id, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{weekly_goal_id}")
async def update_weekly_goal(
    weekly_goal_id: str,
    weekly_goal: weekly_goal_models.OptionalWeeklyGoal,
    supabase: supabase_dep.SupabaseDep,
) -> weekly_goal_models.WeeklyGoalInDB:
    try:
        res = await weekly_goal_crud_handler.update_weekly_goal(weekly_goal_id, weekly_goal, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{weekly_goal_id}")
async def delete_weekly_goal(
    weekly_goal_id: str, supabase: supabase_dep.SupabaseDep
) -> weekly_goal_models.WeeklyGoalInDB:
    try:
        res = await weekly_goal_crud_handler.delete_weekly_goal(weekly_goal_id, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))
