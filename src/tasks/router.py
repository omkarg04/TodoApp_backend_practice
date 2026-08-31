from fastapi import APIRouter ,Depends , status
from src.utils.db import get_db
from src.tasks import controller
from src.tasks.dtos import TaskSchemaDTO ,TaskResponseSchemaDTO
from typing import List
from sqlalchemy.orm import Session



task_routes =APIRouter(prefix="/tasks")

@task_routes.post("/create",response_model=TaskResponseSchemaDTO,status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchemaDTO ,db:Session = Depends(get_db)):
    return controller.create_task(body,db)

@task_routes.get("/get_tasks" ,response_model=List[TaskResponseSchemaDTO], status_code=status.HTTP_200_OK)
def get_tasks(db:Session = Depends(get_db)):
    return controller.get_tasks(db)

@task_routes.get("/get_one_task/{task_id}",response_model=TaskResponseSchemaDTO, status_code=status.HTTP_200_OK)
def get_one_task(task_id:int,db:Session = Depends(get_db)):
    return controller.get_one_task(task_id,db)

@task_routes.put("/update_task/{task_id}",response_model=TaskResponseSchemaDTO, status_code=status.HTTP_201_CREATED)
def update_task(body:TaskSchemaDTO ,task_id:int,db:Session = Depends(get_db)):
    return controller.update_task(body,task_id,db)

@task_routes.delete("/delete_task/{task_id}",response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db:Session = Depends(get_db)):
    return controller.delete_task(task_id,db)