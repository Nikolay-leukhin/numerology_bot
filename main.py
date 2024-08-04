import asyncio

from aiogram import Bot, Dispatcher
from bot.handlers.app import router as app_router
from bot.handlers.payment import router as payment_router
from bot.keyboards.webapp_keyboard import Keyboards
from config.config import load_config


async def main():
    cfg = load_config()

    bot: Bot = Bot(cfg.tg_bot.bot_token)
    dp: Dispatcher = Dispatcher()

    dp.include_router(app_router)
    dp.include_router(payment_router)

    await bot.set_my_commands(Keyboards.main_menu)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
