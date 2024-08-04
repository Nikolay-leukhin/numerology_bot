from typing import List

from aiogram.filters.callback_data import CallbackData


class CreateInvoiceCallBack(CallbackData, prefix='create_invoice'):
    name: str


