from aiogram.fsm.state import StatesGroup, State


class FSMPayment(StatesGroup):
    payment_list = State()
    choose_payment = State()
    selected_payment = State()
    buy = State()

