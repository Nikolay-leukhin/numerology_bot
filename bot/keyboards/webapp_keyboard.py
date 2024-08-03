from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


class Keyboards:
    @staticmethod
    def web_keyboard():
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Перейти!',
                        web_app=WebAppInfo(url="https://fascinating-sable-89d740.netlify.app/")
                    )
                ]
            ]
        )
