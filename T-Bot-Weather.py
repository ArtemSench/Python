import telebot
import requests

# Токен от BotFather
TELEGRAM_API_TOKEN = ''
# API-ключ от WeatherAPI
WEATHER_API_KEY = '2a34c5683466463ab94105743241906'

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = data['location']['name']
        country = data['location']['country']
        last_updated = data['current']["last_updated"]
        temp_c = data['current']['temp_c']
        feelslike = data['current']['feelslike_c']
        cloud = data['current']['cloud']
        humidity = data['current']['humidity']
        wind_kph = data['current']['wind_kph']
        wind_ms = round(wind_kph*0.278, 2)
        return (f'Погода в {location}, {country}:\n'
                f'Последнее обновление: {last_updated}\n'
                f'Температура: {temp_c}°C\n'
                f'Ощущается как: {feelslike}°C\n'
                f'Облачность: {cloud}\n'
                f'Влажность: {humidity}%\n'
                f'Скорость ветра: {wind_ms} м/с')
    else:
        return "Не удалось получить данные о погоде. Пожалуйста, проверьте название города."

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который предоставляет информацию о погоде. Введите название города, чтобы узнать текущую погоду.")

@bot.message_handler(func=lambda message: True)
def send_weather(message):
    city = message.text
    weather_info = get_weather(city)
    bot.reply_to(message, weather_info)

if __name__ == "__main__":
    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    bot.polling(none_stop=True)
