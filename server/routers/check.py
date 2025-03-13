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


@router.patch("/{weekly_goal_id}/check")
async def check_weekly_goal(
    weekly_goal_id: str, supabase: supabase_dep.SupabaseDep
) -> weekly_goal_models.WeeklyGoalInDB:
    try:
        res = await check_handler.check_weekly_goal(weekly_goal_id, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{weekly_goal_id}/uncheck")
async def uncheck_weekly_goal(
    weekly_goal_id: str, supabase: supabase_dep.SupabaseDep
) -> weekly_goal_models.WeeklyGoalInDB:
    try:
        res = await check_handler.uncheck_weekly_goal(weekly_goal_id, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{weekly_goal_id}/last_check")
async def get_last_check(weekly_goal_id: str, supabase: supabase_dep.SupabaseDep) -> datetime.datetime | None:
    try:
        res = await check_handler.get_last_check(weekly_goal_id, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))
