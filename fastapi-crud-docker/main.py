# main.py
from fastapi import FastAPI
from typing import List
from app.models import User
import app.crud as crud

app = FastAPI()

@app.post("/users/", response_model=User)
def create_user(user: User):
    return crud.create_user(user)

@app.get("/users/", response_model=List[User])
def read_users():
    return crud.read_users()

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    return crud.read_user(user_id)

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    return crud.update_user(user_id, user)

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    crud.delete_user(user_id)
    return {"detail": "User deleted"}
#ci integeration