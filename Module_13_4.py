from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

import asyncio

api = '7284766138:AAFyDMzDLXAAwcm9NT32BC1dhxPX12fw_V4'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text=['/start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.\n'
                         'Введите команду /Calories для рассчета нормы калорий')

@dp.message_handler(text = ['/Calories'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age1=message.text)
    data = await state.get_data()
    await message.answer('Введите свой рост (см):')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth1=message.text)
    data = await state.get_data()
    await message.answer('Введите свой вес (кг):')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight1=message.text)
    data = await state.get_data()
    await message.answer(f"Вам необходимо следующее количество килокалорий (ккал) в сутки: {10*int(data['weight1'])+6.25*int(data['growth1'])-5*int(data['age1'])+5}")
    await state.finish()

@dp.message_handler()
async def echo_message(message):
    await message.answer(f'вы написали мне: {message.text}\n'
                         f'Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)