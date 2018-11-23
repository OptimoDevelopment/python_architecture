from dataclasses import dataclass, field
from datetime import datetime
from typing import List


class Base:
    pass


@dataclass
class Client(Base):
    id: int
    name: str


@dataclass
class Product(Base):
    id: int
    name: str
    price: float


@dataclass
class Order(Base):
    id: int
    created: datetime
    client: Client
    total_cost: float = 0
    items: List[Product] = field(default_factory=list)
