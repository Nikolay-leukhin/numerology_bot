import asyncio

from aiogram import Bot, Dispatcher
from bot.handlers.app import router as app_router
from bot.handlers.payment import router as payment_router


async def main():
    bot: Bot = Bot("7203647961:AAGJioNjlLllwtoxeK_hJooHy6V9VX1zZXw")
    dp: Dispatcher = Dispatcher()

    dp.include_router(app_router)
    dp.include_router(payment_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)




if __name__ == '__main__':
    asyncio.run(main())
