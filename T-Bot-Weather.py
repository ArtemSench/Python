import requests
import queue
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Функция для /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Отправь мне сообщение, и я повторю его.')

# Функция для обработки сообщений
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    # Токен, полученный от https://t.me/BotFather
    token = '7386171008:AAFTNGv9f_5xCHMHpcFT9YOjP8DVF3Bj-GM'

    # Создаем Updater и передаем ему токен
    updater = Updater(token)

    # Получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчик для команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик для всех текстовых сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при завершении работы
    updater.idle()

if __name__ == '__main__':
    main()
