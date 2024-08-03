import dataclasses
from typing import List


@dataclasses.dataclass
class SubscriptionModel:
    name: str
    price: int
    description_list: List[str]

