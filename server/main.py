import sys
import pathlib

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

sys.path.append(str(pathlib.Path(__file__).parent))
from routers import goal_crud, week_crud, weekly_goal_crud

origins = []

origins.extend(
    [
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:8085",
    ]
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    goal_crud.router,
    prefix="/goal",
    tags=["Goal"],
)

app.include_router(
    week_crud.router,
    prefix="/week",
    tags=["Week"],
)

app.include_router(
    weekly_goal_crud.router,
    prefix="/weekly_goal",
    tags=["Weekly Goal"],
)


@app.get("/", tags=["Root"])
async def redirect_root_to_docs():
    return RedirectResponse("/docs")
