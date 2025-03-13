import uuid
import datetime

from pydantic import BaseModel, Field


class WeeklyGoal(BaseModel):
    goal_id: uuid.UUID = Field()
    week_id: uuid.UUID = Field()
    progress: int = Field(default=0)  # Temp deprecated
    check_history: list[datetime.datetime] = Field(default=[])  # Temp deprecated
    mon: bool = Field(default=False)
    tue: bool = Field(default=False)
    wed: bool = Field(default=False)
    thu: bool = Field(default=False)
    fri: bool = Field(default=False)
    sat: bool = Field(default=False)
    sun: bool = Field(default=False)


class WeeklyGoalInDB(WeeklyGoal):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)


class OptionalWeeklyGoal(BaseModel):
    goal_id: uuid.UUID | None = None
    week_id: uuid.UUID | None = None
    progress: int | None = None
    check_history: list[datetime.datetime] | None = None
    mon: bool = Field(default=False)
    tue: bool = Field(default=False)
    wed: bool = Field(default=False)
    thu: bool = Field(default=False)
    fri: bool = Field(default=False)
    sat: bool = Field(default=False)
    sun: bool = Field(default=False)
