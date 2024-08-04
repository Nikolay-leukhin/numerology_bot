from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards.webapp_keyboard import Keyboards
from bot.lexicon.lexicon import Lexicon
from bot.states.payments_fsm import FSMPayment

router = Router()


@router.message(CommandStart())
async def process_start(msg: Message):
    await msg.reply(text=Lexicon.start, reply_markup=Keyboards.start_keyboard())


@router.message(Command(commands="app"))
async def process_open_app(msg: Message):
    await msg.reply(text=Lexicon.open_app, reply_markup=Keyboards.webapp_keyboard())


@router.message(Command(commands="buy"))
async def process_buy(msg: Message):
    await msg.reply(text=Lexicon.buy_command, reply_markup=Keyboards.choose_subscription())
