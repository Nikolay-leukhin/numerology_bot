from typing import List

from models.subscription import SubscriptionModel


class SubscriptionRepository:
    subs: List[SubscriptionModel] = [
        SubscriptionModel(
            name="Разовый",
            price=390,
            description_list=[
                "Полная расшифровка одной матрицы",
                "Доступ сразу после оплаты"
            ]
        ),
        SubscriptionModel(
            name="Пробный",
            price=690,
            description_list=[
                "Доступ на неделю",
                "Полная расшифровка двух личных матриц",
                "Доступ сразу после оплаты"
            ]
        ),
        SubscriptionModel(
            name="Месячный",
            price=2290,
            description_list=[
                "Доступ на месяц",
                "Безлимитное количество расшифровок матриц",
                "Доступ сразу после оплаты"
            ]
        ),
        SubscriptionModel(
            name="Годовой",
            price=8390,
            description_list=[
                "Доступ на год",
                "Безлимитное количество расшифровок матриц",
                "Доступ сразу после оплаты"
            ]
        )
    ]
