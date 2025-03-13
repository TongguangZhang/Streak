import sys
import pathlib

from fastapi import APIRouter, HTTPException

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from config import root_logger
from dependencies import supabase_dep
from models import week_models
from services import week_admin_handler
from responses import week_admin_responses


router = APIRouter()


# ==========================================
# Business logic for weeks
# ==========================================


@router.post("/new_week")
async def create_new_week(supabase: supabase_dep.SupabaseDep) -> week_models.WeekInDB:
    try:
        res = await week_admin_handler.create_new_week(supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/latest_week")
async def get_latest_week(supabase: supabase_dep.SupabaseDep) -> week_models.WeekInDB:
    try:
        res = await week_admin_handler.get_latest_week(supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{week_id}")
async def get_weekly_goals(
    week_id: str, supabase: supabase_dep.SupabaseDep
) -> list[week_admin_responses.CombinedGoal]:
    try:
        res = await week_admin_handler.get_weekly_goals(week_id, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))
