import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from database.db import init_db
from handlers import start, add, list, get, delete


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(add.router)
    dp.include_router(list.router)
    dp.include_router(get.router)
    dp.include_router(delete.router)

    await init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())