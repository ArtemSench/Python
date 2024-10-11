from fastapi import FastAPI, HTTPException, Path, Request
from typing import Dict, Annotated
from pydantic import BaseModel
from typing import List
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# Список пользователей
users = []

@app.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "user_list": users})


@app.get("/users/{user_id}", response_class=HTMLResponse)
async def read_user(request: Request, user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})

# Удаление пользователя
@app.delete("/user/{user_id}", response_model=User)
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            return users.pop(index)
    raise HTTPException(status_code=404, detail="User was not found")

# Создание пользователя
@app.post("/user/{username}/{age}", response_model=User)
def add_users(
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

