import uuid
import datetime

from pydantic import BaseModel, Field


def get_monday():
    today = datetime.date.today()
    return today - datetime.timedelta(days=today.weekday())


class Week(BaseModel):
    completed: bool = Field(default=False)
    start_date: datetime.date = Field(default_factory=lambda: get_monday())


class WeekInDB(Week):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)


class OptionalWeek(BaseModel):
    completed: bool | None = None
    start_date: datetime.date | None = None
