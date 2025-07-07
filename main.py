from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from models import Task
from schemas import TaskCreate, TaskUpdate, TaskResponse
from database import SessionLocal, engine, Base
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title = "Task Manager API")

@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate):
    return crud.create_task(task)

@app.get("/tasks", response_model=List[TaskResponse])
def get_tasks(is_completed: Optional[bool] = Query(None)):
    return crud.get_all_tasks(is_completed)

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    task = crud.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate):
    updated = crud.update_task(task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    success = crud.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}

@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}