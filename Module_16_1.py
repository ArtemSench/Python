from fastapi import FastAPI

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
async def user_number(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Определяем маршрут для страниц пользователей с передачей данных в адресной строке
@app.get("/user")
async def user_info(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}