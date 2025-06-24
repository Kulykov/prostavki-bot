from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
import logging
import asyncio
import os
from datetime import datetime

API_TOKEN = os.getenv('API_TOKEN')
ADMIN_CHAT_ID = int(os.getenv('ADMIN_CHAT_ID'))

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

strategies = [
    "🎯 Ставь на live-тоталы после 10-й минуты — анализируй динамику матча!",
    "📊 Используй догон на ничью в лайве — особенно в равных по силам лигах.",
    "🚀 Перестраховка: ставь 70% на фаворита и 30% на ничью в двойных шансах.",
    "📉 Играем на понижение: тотал меньше в затяжных матчах с малым количеством ударов."
]

main_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📈 Стратегия дня")]
], resize_keyboard=True)

@router.message(F.text == "/start")
async def start_cmd(message: types.Message):
    await message.answer(
        "👋 Добро пожаловать в ProStavki | Profit!",
        reply_markup=main_menu
    )

@router.message(F.text == "📈 Стратегия дня")
async def strategy_day(message: types.Message):
    day_index = datetime.now().day % len(strategies)
    await message.answer(f"📊 Стратегия на сегодня:\n{strategies[day_index]}")

if __name__ == '__main__':
    async def main():
        dp.include_router(router)
        await dp.start_polling(bot)
    asyncio.run(main())