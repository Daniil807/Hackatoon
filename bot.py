import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message 

from config import TOKKEN 

bot = Bot(token=TOKKEN)
dp = Dispatcher()

(dp.message(CommandStart))
async def cmd_start(message: Message):
    await message.answer("Привет")
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main_":
    asyncio.run(main())