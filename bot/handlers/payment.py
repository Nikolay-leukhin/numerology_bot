from aiogram import types
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram import F

from bot.callback_factories.create_invoice_callback import CreateInvoiceCallBack
from bot.callback_factories.subscription_callback_factory import SubCallBack
from bot.keyboards.webapp_keyboard import Keyboards
from bot.lexicon.lexicon import Lexicon
from data.subscription_repository import SubscriptionRepository

from config.config import load_config

cfg = load_config()
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

    await cb.message.edit_text(text=text, reply_markup=Keyboards.detailed_subscription(sub))
    await cb.answer()


@router.callback_query(lambda cb: cb.data == "go_back")
async def show_subscriptions(cb: CallbackQuery):
    await cb.message.delete()
    await cb.answer()


@router.callback_query(CreateInvoiceCallBack.filter())
async def show_subscriptions(cb: CallbackQuery, callback_data: CreateInvoiceCallBack):
    pay_token = cfg.tg_bot.payment_token
    sub = list(filter(lambda item: item.name == callback_data.name, SubscriptionRepository.subs))[0]

    await cb.bot.send_invoice(cb.message.chat.id,
                              title=f"Тариф: {sub.name}",
                              description=sub.description_list[0],
                              provider_token=pay_token,
                              currency="rub",
                              photo_url="https://cdn.britannica.com/72/223172-131-C3F72804/astrology-horoscope-circle.jpg",
                              photo_width=416,
                              photo_height=234,
                              photo_size=416,
                              is_flexible=False,
                              prices=[types.LabeledPrice(label=f"Подписка на {sub.name}", amount=sub.price * 100)],
                              start_parameter="one-month-subscription",
                              payload="test-invoice-payload")

    await cb.answer()


# 1111 1111 1111 1026, 12/22, CVC 000.
#

@router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await pre_checkout_q.bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@router.message(F.successful_payment)
async def successful_payment(message: types.Message):
    await message.bot.send_message(
        message.chat.id,
        f"🎉 Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно! 🥳💰",
        reply_markup=Keyboards.webapp_keyboard()
    )
