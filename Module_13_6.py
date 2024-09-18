from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

api = '7284766138:AAFyDMzDLXAAwcm9NT32BC1dhxPX12fw_V4'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

ikb = InlineKeyboardMarkup(resize_keyboard=True)
calc_ib = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
formula_ib = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')

ikb.row(calc_ib, formula_ib)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_button = KeyboardButton(text="Информация")
calc_button = KeyboardButton(text='Рассчитать')

kb.row(start_button, calc_button)

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=ikb)

@dp.callback_query_handler(text='formulas')
async def get_formula(call):
    await call.message.answer('Упрощенный вариант формулы Миффлина-Сан Жеора: \n'
                              '10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()



@dp.message_handler(text=['/start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text="Информация")
async def info_message(message):
    await message.answer('Нажмите кнопку "Рассчитать" для рассчета нормы калорий', reply_markup=kb)


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    if message.text.isdigit():  # Проверяем, является ли ввод числом
        await state.update_data(age1=int(message.text))  # Сохраняем возраст как число
        await message.answer('Введите свой рост (см):')
        await UserState.growth.set()
    else:
        await message.answer('Пожалуйста, введите корректный возраст (число).')

@dp.message_handler(state = UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    if message.text.isdigit():  # Проверяем, является ли ввод числом
        await state.update_data(growth1=int(message.text))  # Сохраняем рост как число
        await message.answer('Введите свой вес (кг):')
        await UserState.weight.set()
    else:
        await message.answer('Пожалуйста, введите корректный рост (число).')

@dp.message_handler(state = UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    if message.text.isdigit():  # Проверяем, является ли ввод числом
        await state.update_data(weight1=int(message.text))  # Сохраняем вес как число
        data = await state.get_data()
        # Рассчитываем количество калорий
        calories = 10 * data['weight1'] + 6.25 * data['growth1'] - 5 * data['age1'] + 5
        await message.answer(f"Вам необходимо следующее количество килокалорий (ккал) в сутки: {calories}")
        await state.finish()
    else:
        await message.answer('Пожалуйста, введите корректный вес (число).')

@dp.message_handler()
async def echo_message(message):
    await message.answer(f'Зачем вы написали мне?: {message.text}\n'
                         f'Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)