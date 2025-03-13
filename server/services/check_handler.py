import sys
import pathlib
import datetime

from supabase import AClient

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from models import weekly_goal_models
from services import weekly_goal_crud_handler


async def check_weekly_goal(weekly_goal_id: str, supabase: AClient) -> weekly_goal_models.WeeklyGoalInDB:
    weekly_goal = await weekly_goal_crud_handler.get_weekly_goal(weekly_goal_id, supabase)

    weekly_goal.progress += 1
    weekly_goal.check_history.append(datetime.datetime.now())

    weekly_goal = await weekly_goal_crud_handler.update_weekly_goal(weekly_goal_id, weekly_goal, supabase)
    return weekly_goal


async def uncheck_weekly_goal(weekly_goal_id: str, supabase: AClient) -> weekly_goal_models.WeeklyGoalInDB:
    weekly_goal = await weekly_goal_crud_handler.get_weekly_goal(weekly_goal_id, supabase)

    weekly_goal.progress -= 1
    weekly_goal.check_history.pop()

    weekly_goal = await weekly_goal_crud_handler.update_weekly_goal(weekly_goal_id, weekly_goal, supabase)
    return weekly_goal


async def get_last_check(weekly_goal_id: str, supabase: AClient) -> datetime.datetime | None:
    weekly_goal = await weekly_goal_crud_handler.get_weekly_goal(weekly_goal_id, supabase)
    if weekly_goal.check_history:
        return weekly_goal.check_history[-1]
    return None
