from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '7284766138:AAFyDMzDLXAAwcm9NT32BC1dhxPX12fw_V4'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text=['/start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def echo_message(message):
     print(f'вы написали мне:{message.text}')
     await message.answer(f'вы написали мне: {message.text}\n'
                          f'Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)