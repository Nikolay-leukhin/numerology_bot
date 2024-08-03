from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from bot.callback_factories.subscription_callback_factory import SubCallBack
from data.subscription_repository import SubscriptionRepository


class Keyboards:
    @staticmethod
    def start_keyboard():
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Перейти!',
                        web_app=WebAppInfo(url="https://fascinating-sable-89d740.netlify.app/")
                    ),
                    InlineKeyboardButton(
                        text='Купить подписку',
                        callback_data='buy_subscription'
                    )
                ]
            ]
        )

    @staticmethod
    def choose_subscription():
        return InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text=f"{item.name} - {item.price}₽",
                                                   callback_data=SubCallBack(name=item.name).pack())] for item in
                             SubscriptionRepository.subs]
        )

    @staticmethod
    def detailed_subscription():
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Назад',
                        callback_data="go_back"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text='Купить',
                        callback_data="buy_sub"
                    ),
                ]
            ]
        )

