import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = 8418790613:AAGOse1hUhem7H1XjAFgCODoK88EN16cqp0

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет, братан! Бот работает 🚀")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
