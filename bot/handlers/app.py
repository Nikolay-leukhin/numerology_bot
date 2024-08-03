from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message

from bot.keyboards.webapp_keyboard import Keyboards
from bot.lexicon.lexicon import Lexicon

router = Router()


@router.message(CommandStart())
async def process_start(msg: Message):
    await msg.reply(text=Lexicon.start, reply_markup=Keyboards.start_keyboard())
