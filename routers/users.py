from fastapi import Body
from fastapi import APIRouter, Depends
from core.database import db
from typing import List
from models.user import User
from core.auth import get_current_user
# Route to fetch a particular user by id
from fastapi import HTTPException
from uuid import UUID


router = APIRouter()


# POST route to add a new user
@router.post("/users", response_model=User)
async def create_user(
    username: str = Body(...),
    hashed_password: str = Body(...),
    fullname: str = Body(...),
    emailaddress: str = Body(...),
    phonenumber: str = Body(...),
    current_user: dict = Depends(get_current_user)
):
    from models.user import User
    from uuid import uuid4
    user = User(
        id=str(uuid4()),
        username=username,
        hashed_password=hashed_password,
        fullname=fullname,
        emailaddress=emailaddress,
        phonenumber=phonenumber
    )
    user_dict = user.dict(by_alias=True)
    await db["users"].insert_one(user_dict)
    return user



@router.get("/users", response_model=List[User])
async def list_users(current_user: dict = Depends(get_current_user)):
    print(f"Current user: {current_user}")
    users_cursor = db["users"].find({}, {"_id": 1, "username": 1, "hashed_password": 1})
    users = await users_cursor.to_list(length=100)
    print(f"Fetched users: {users}")
    return users




@router.get("/users/{id}", response_model=User)
async def get_user_by_id(id: UUID, current_user: dict = Depends(get_current_user)):
    print("id: ", id)
    user = await db["users"].find_one({"_id": str(id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
