import uuid
import datetime

from pydantic import BaseModel, Field


class GoalHistory(BaseModel):
    start: datetime.datetime = Field(default_factory=datetime.datetime.now)
    end: datetime.datetime | None = Field(default=None)
    count: int = Field(default=1)


class Goal(BaseModel):
    active: bool = Field(default=False)
    name: str = Field(default="New Goal")
    description: str | None = Field(default=None)
    count: int = Field(default=1)
    history: list[GoalHistory] = Field(default_factory=list)


class GoalInDB(Goal):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)


class OptionalGoal(BaseModel):
    active: bool | None = None
    name: str | None = None
    description: str | None = None
    count: int | None = None
    history: list[GoalHistory] | None = None
