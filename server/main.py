import sys
import pathlib

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

sys.path.append(str(pathlib.Path(__file__).parent))
from routers import goal_crud, week_crud, weekly_goal_crud, week_admin, check

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
    prefix="/goal_crud",
    tags=["Goal"],
)

app.include_router(
    week_crud.router,
    prefix="/week_crud",
    tags=["Week"],
)

app.include_router(
    weekly_goal_crud.router,
    prefix="/weekly_goal_crud",
    tags=["Weekly Goal"],
)

app.include_router(
    week_admin.router,
    prefix="/week_admin",
    tags=[
        "Week Admin",
    ],
)


app.include_router(
    check.router,
    prefix="/check",
    tags=["Check"],
)


@app.get("/", tags=["Root"])
async def redirect_root_to_docs():
    return RedirectResponse("/docs")
