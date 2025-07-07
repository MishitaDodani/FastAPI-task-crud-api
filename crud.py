from sqlalchemy.orm import Session
from database import SessionLocal
from models import Task
from schemas import TaskCreate, TaskUpdate

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_task(task: TaskCreate):
    db = SessionLocal()
    db_task = Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_all_tasks(is_completed=None):
    db = SessionLocal()
    if is_completed is not None:
        return db.query(Task).filter(Task.is_completed == is_completed).all()
    return db.query(Task).all()

def get_task(task_id: int):
    db = SessionLocal()
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(task_id: int, task: TaskUpdate):
    db = SessionLocal()
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        for field, value in task.model_dump().items():
            setattr(db_task, field, value)
        db.commit()
        db.refresh(db_task)
        return db_task
    return None

def delete_task(task_id: int):
    db = SessionLocal()
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False
