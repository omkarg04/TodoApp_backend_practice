from fastapi import FastAPI
from src.utils.db import Base,engine
from src.tasks.models import TaskModel
from src.tasks.router import task_routes



Base.metadata.create_all(engine)

app = FastAPI(title="This is my Todo app")
app.include_router(task_routes)