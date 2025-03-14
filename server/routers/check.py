import sys
import pathlib
import datetime

from fastapi import APIRouter, HTTPException

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from config import root_logger
from dependencies import supabase_dep
from models import weekly_goal_models
from services import check_handler

router = APIRouter()


# ==========================================
# Business logic for checking
# ==========================================


@router.patch("/{weekly_goal_id}/check_day")
async def check_day(
    weekly_goal_id: str, day: str, supabase: supabase_dep.SupabaseDep
) -> weekly_goal_models.WeeklyGoalInDB:
    try:
        res = await check_handler.check_day(weekly_goal_id, day, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{weekly_goal_id}/uncheck_day")
async def uncheck_day(
    weekly_goal_id: str, day: str, supabase: supabase_dep.SupabaseDep
) -> weekly_goal_models.WeeklyGoalInDB:
    try:
        res = await check_handler.uncheck_day(weekly_goal_id, day, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))
