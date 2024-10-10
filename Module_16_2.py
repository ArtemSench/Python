from fastapi import FastAPI, Path
from typing import Annotated

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определяем маршрут для главной страницы
@app.get("/")
async def main_page():
    return {"message": "Главная страница"}

# Определяем маршрут для страницы администратора
@app.get("/user/admin")
async def admin_page():
    return {"message": "Вы вошли как администратор"}

# Определяем маршрут для страниц пользователей с параметром в пути
@app.get("/user/{user_id}")
async def user_number(
    user_id: Annotated[int, Path(
        ge=1, le=100, description="Enter User ID"
    )]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Определяем маршрут для страниц пользователей с передачей данных в адресной строке
@app.get("/user/{username}/{age}")
async def user_info(
    username: Annotated[str, Path(
        min_length=5, max_length=20, description="Enter username"
    )],
    age: Annotated[int, Path(
        ge=18, le=120, description="Enter age"
    )]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}