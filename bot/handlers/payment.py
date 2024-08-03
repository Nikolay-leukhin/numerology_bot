from aiogram import types
from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery

from bot.callback_factories.subscription_callback_factory import SubCallBack
from bot.keyboards.webapp_keyboard import Keyboards
from bot.lexicon.lexicon import Lexicon
from data.subscription_repository import SubscriptionRepository

router = Router()


@router.callback_query(lambda cb: cb.data == "buy_subscription")
async def show_subscriptions(cb: CallbackQuery):
    await cb.message.answer(text=Lexicon.buy_sub, reply_markup=Keyboards.choose_subscription())
    await cb.answer()


@router.callback_query(SubCallBack.filter())
async def show_subscriptions_details(cb: CallbackQuery, callback_data: SubCallBack):
    sub = list(filter(lambda item: item.name == callback_data.name, SubscriptionRepository.subs))[0]
    text = (
            f"🔮 {sub.name} - {sub.price}₽\n\n"
            f"Описание:\n\n"
            + '\n'.join([f"⭐️ - {desc}" for desc in sub.description_list])
    )

    await cb.message.answer(text=text, reply_markup=Keyboards.detailed_subscription())
    await cb.answer()


@router.callback_query(lambda cb: cb.data == "go_back")
async def show_subscriptions(cb: CallbackQuery):
    await cb.message.delete()
    await cb.answer()


@router.callback_query(lambda cb: cb.data == "buy_sub")
async def show_subscriptions(cb: CallbackQuery):
    pay_token = "381764678:TEST:91523"

    await cb.bot.send_invoice(cb.message.chat.id,
                              title="подписка на звезды",
                              description="Активация подписки на звезды на 1 месяц",
                              provider_token=pay_token,
                              currency="rub",
                              photo_url="https://1poppers.ru/wp-content/uploads/2015/03/stretch-6.jpg",
                              photo_width=416,
                              photo_height=234,
                              photo_size=416,
                              is_flexible=False,
                              prices=[types.LabeledPrice(label="Подписка на 1 месяц", amount=500 * 100)],
                              start_parameter="one-month-subscription",
                              payload="test-invoice-payload")

    await cb.answer()


@router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await pre_checkout_q.bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

