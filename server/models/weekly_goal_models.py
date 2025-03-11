import uuid
import datetime

from pydantic import BaseModel, Field


class WeeklyGoal(BaseModel):
    goal_id: uuid.UUID = Field()
    week_id: uuid.UUID = Field()
    progress: int = Field(default=0)
    check_history: list[datetime.datetime] = Field(default=[])


class WeeklyGoalInDB(WeeklyGoal):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)


class OptionalWeeklyGoal(BaseModel):
    goal_id: uuid.UUID | None = None
    week_id: uuid.UUID | None = None
    progress: int | None = None
    check_history: list[datetime.datetime] | None = None
