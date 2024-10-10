# app/crud.py
from typing import List, Dict
from fastapi import HTTPException
from .models import User

fake_db: Dict[int, User] = {}
next_id = 1

def create_user(user: User) -> User:
    global next_id
    user_id = next_id
    fake_db[user_id] = user
    next_id += 1
    return user

def read_users() -> List[User]:
    return list(fake_db.values())

def read_user(user_id: int) -> User:
    user = fake_db.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def update_user(user_id: int, user: User) -> User:
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    fake_db[user_id] = user
    return user

def delete_user(user_id: int) -> None:
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    del fake_db[user_id]
