from fastapi import APIRouter, Depends, HTTPException
from fastapi import BackgroundTasks
from core.celery_worker import sample_task, celery_app
from typing import List
from core.auth import get_current_user

router = APIRouter(tags=["medicines"])

# Example: List all medicines
@router.get("/medicines", response_model=List[dict])
async def list_medicines(current_user: dict = Depends(get_current_user)):
    # Placeholder: Replace with actual DB logic
    return []

# Example: Add a new medicine
@router.post("/medicines", response_model=dict)
async def add_medicine(name: str, description: str, current_user: dict = Depends(get_current_user)):
    # Placeholder: Replace with actual DB logic
    return {"name": name, "description": description}


# Route to trigger a sample celery task
@router.post("/medicines/sample-task")
async def trigger_sample_task(x: int, y: int):
    task = sample_task.delay(x, y)
    return {"task_id": task.id}

# Route to check celery task result
@router.get("/medicines/sample-task/{task_id}")
async def get_sample_task_result(task_id: str):
    result = celery_app.AsyncResult(task_id)
    return {"task_id": task_id, "status": result.status, "result": result.result}
