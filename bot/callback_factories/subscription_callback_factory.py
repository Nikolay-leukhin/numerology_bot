from typing import List

from aiogram.filters.callback_data import CallbackData


class SubCallBack(CallbackData, prefix='sub'):
    name: str
