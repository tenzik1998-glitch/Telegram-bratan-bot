import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = 8283615044:AAEjYP2JTZO4LI-AZ3ESEnXyvlLzf6FCLwc

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
