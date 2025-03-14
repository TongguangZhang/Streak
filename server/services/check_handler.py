import sys
import pathlib
import datetime

from supabase import AClient

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from models import weekly_goal_models
from services import weekly_goal_crud_handler

# ==========================================
# Business logic for checking
# ==========================================


async def check_day(weekly_goal_id: str, day: str, supabase: AClient) -> weekly_goal_models.WeeklyGoalInDB:
    weekly_goal = await weekly_goal_crud_handler.get_weekly_goal(weekly_goal_id, supabase)

    weekly_goal.__setattr__(day, True)
    weekly_goal.progress += 1

    weekly_goal = await weekly_goal_crud_handler.update_weekly_goal(weekly_goal_id, weekly_goal, supabase)
    return weekly_goal


async def uncheck_day(weekly_goal_id: str, day: str, supabase: AClient) -> weekly_goal_models.WeeklyGoalInDB:
    weekly_goal = await weekly_goal_crud_handler.get_weekly_goal(weekly_goal_id, supabase)

    weekly_goal.__setattr__(day, False)
    weekly_goal.progress -= 1

    weekly_goal = await weekly_goal_crud_handler.update_weekly_goal(weekly_goal_id, weekly_goal, supabase)
    return weekly_goal
