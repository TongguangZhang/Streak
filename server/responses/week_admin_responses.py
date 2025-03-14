import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent))
from models import goal_models, weekly_goal_models, week_models


class CombinedGoal(goal_models.GoalInDB, weekly_goal_models.WeeklyGoalInDB):
    pass


class WeekData(week_models.WeekInDB):
    total_set: int = 0
    total_achieved: int = 0
