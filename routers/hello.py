from fastapi import APIRouter, Depends
from core.database import db
from core.auth import get_current_user

router = APIRouter()

@router.get("/hello")
async def read_hello(current_user: dict = Depends(get_current_user)):
    collections = await db.list_collection_names()
    return {"message": "Hello, World!", "collections": collections, "user": current_user["sub"]}
