import sys
import pathlib

from fastapi import APIRouter, HTTPException

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from config import root_logger
from dependencies import supabase_dep
from models import week_models
from services import week_handler


router = APIRouter()

# ==========================================
# CRUD for week
# ==========================================


@router.post("/")
async def create_week(week: week_models.Week, supabase: supabase_dep.SupabaseDep) -> week_models.WeekInDB:
    try:
        res = await week_handler.create_week(week, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{week_id}")
async def get_week(week_id, supabase: supabase_dep.SupabaseDep) -> week_models.WeekInDB:
    try:
        res = await week_handler.get_week(week_id, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{week_id}")
async def update_week(
    week_id: str,
    week: week_models.OptionalWeek,
    supabase: supabase_dep.SupabaseDep,
) -> week_models.WeekInDB:
    try:
        res = await week_handler.update_week(week_id, week, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{week_id}")
async def delete_week(week_id: str, supabase: supabase_dep.SupabaseDep) -> week_models.WeekInDB:
    try:
        res = await week_handler.delete_week(week_id, supabase)
        return res
    except Exception as e:
        root_logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))
