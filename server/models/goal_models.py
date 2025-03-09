import uuid
import datetime

from pydantic import BaseModel, Field


class Goal(BaseModel):
    active: bool = Field(default=True)
    name: str = Field(default="New Goal")
    description: str | None = Field(default=None)
    count: int = Field(default=0)


class GoalInDB(Goal):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    deactivated_at: datetime.datetime | None = Field(default=None)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)


class OptionalGoal(BaseModel):
    active: bool | None = None
    name: str | None = None
    description: str | None = None
    count: int | None = None
