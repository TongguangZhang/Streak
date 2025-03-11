import sys
import pathlib

from fastapi.encoders import jsonable_encoder
from supabase import AClient, PostgrestAPIResponse

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from models import week_models, weekly_goal_models, goal_models

# ==========================================
# CRUD Handlers for week
# ==========================================


async def create_week(week: week_models.Week, supabase: AClient) -> week_models.WeekInDB:
    res: PostgrestAPIResponse = await supabase.table("week").insert(jsonable_encoder(week)).execute()
    week = week_models.WeekInDB(**res.data[0])
    return week


async def get_week(week_id: str, supabase: AClient) -> week_models.WeekInDB:
    res: PostgrestAPIResponse = await supabase.table("week").select("*").eq("id", week_id).execute()
    week = week_models.WeekInDB(**res.data[0])
    return week


async def update_week(week_id: str, week_update: week_models.OptionalWeek, supabase: AClient) -> week_models.WeekInDB:
    res: PostgrestAPIResponse = await (
        supabase.table("week")
        .update(jsonable_encoder(week_update.model_dump(exclude_none=True)))
        .eq("id", week_id)
        .execute()
    )
    week = week_models.WeekInDB(**res.data[0])
    return week


async def delete_week(week_id: str, supabase: AClient) -> week_models.WeekInDB:
    res: PostgrestAPIResponse = await supabase.table("week").delete().eq("id", week_id).execute()
    week = week_models.WeekInDB(**res.data[0])
    return week
