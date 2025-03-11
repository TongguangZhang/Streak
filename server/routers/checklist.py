import sys
import pathlib

from fastapi import APIRouter, HTTPException

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from config import root_logger
from dependencies import supabase_dep
from models import weekly_goal_models, week_models
from services import checklist_handler
from responses import checklist_responses


router = APIRouter()

# ==========================================
# Business logic for checklist
# ==========================================


@router.get("/latest_week")
async def get_latest_week(supabase: supabase_dep.SupabaseDep) -> week_models.WeekInDB:
    try:
        res = await checklist_handler.get_latest_week(supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/new_week")
async def create_new_week(supabase: supabase_dep.SupabaseDep) -> week_models.WeekInDB:
    try:
        res = await checklist_handler.create_new_week(supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{week_id}")
async def get_weekly_goals(week_id: str, supabase: supabase_dep.SupabaseDep) -> list[checklist_responses.CombinedGoal]:
    try:
        res = await checklist_handler.get_weekly_goals(week_id, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{weekly_goal_id}/check")
async def check_weekly_goal(
    weekly_goal_id: str, supabase: supabase_dep.SupabaseDep
) -> weekly_goal_models.WeeklyGoalInDB:
    try:
        res = await checklist_handler.check_weekly_goal(weekly_goal_id, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{weekly_goal_id}/uncheck")
async def uncheck_weekly_goal(
    weekly_goal_id: str, supabase: supabase_dep.SupabaseDep
) -> weekly_goal_models.WeeklyGoalInDB:
    try:
        res = await checklist_handler.uncheck_weekly_goal(weekly_goal_id, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))
