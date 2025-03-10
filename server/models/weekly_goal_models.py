import uuid
import datetime

from pydantic import BaseModel, Field


class WeeklyGoal(BaseModel):
    goal_id: uuid.UUID = Field()
    week_id: uuid.UUID = Field()
    checks: int = Field(default=0)
    completed: bool = Field(default=False)
    last_check: datetime.datetime | None = Field(default=None)


class WeeklyGoalInDB(WeeklyGoal):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)


class OptionalWeeklyGoal(BaseModel):
    goal_id: uuid.UUID | None = None
    week_id: uuid.UUID | None = None
    checks: int | None = None
    completed: bool | None = None
    last_check: datetime.datetime | None = None
