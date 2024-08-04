import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class TelegramConfig:
    bot_token: str
    payment_token: str


@dataclass
class Config:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    tg_bot: TelegramConfig


def load_config() -> Config:
    config = Config(
        tg_bot=TelegramConfig(bot_token=os.environ.get('BOT_TOKEN'), payment_token=os.environ.get('PAYMENT_TOKEN')),
    )
    return config
