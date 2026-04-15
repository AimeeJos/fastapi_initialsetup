from fastapi import APIRouter, Depends, HTTPException
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
