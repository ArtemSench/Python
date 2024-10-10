from fastapi import FastAPI, HTTPException, Path
from typing import Dict, Annotated
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Список пользователей
users = []

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# Получение списка пользователей
@app.get("/users", response_model=List[User])
def get_users():
    return users

# Создание пользователя
@app.post("/user/{username}/{age}", response_model=User)
def create_user(
        username: Annotated[str, Path(min_length=2, max_length=50)],
        age: Annotated[int, Path(ge=6, le=120)]
):
    user_id = (users[-1].id + 1) if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user

# Обновление пользователя
@app.put("/user/{user_id}/{username}/{age}", response_model=User)
def update_user(
    user_id: int,
    username: Annotated[str, Path(min_length=2, max_length=50)],
    age: Annotated[int, Path(ge=6, le=120)]):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# Удаление пользователя
@app.delete("/user/{user_id}", response_model=User)
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            return users.pop(index)
    raise HTTPException(status_code=404, detail="User was not found")