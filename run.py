import asyncio
import logging
from os import getenv
from dotenv import find_dotenv, load_dotenv
from aiogram import Bot, Dispatcher
from app_wending.handlers import router

load_dotenv(find_dotenv())


async def main():
    bot = Bot(token=getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)  # Подключили к диспетчеру роутер из хендлерс
    await dp.start_polling(bot)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
