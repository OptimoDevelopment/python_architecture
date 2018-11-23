from typing import List

from bf_shop.entities import Order
from bf_shop.logic import OrderLogic


def search(logic: OrderLogic, client_id: int) -> List[Order]:
    return logic.search(client_id=client_id)


def create(logic: OrderLogic, body: dict) -> Order:
    return logic.create(client_id=body['client_id'])


def add_product(logic: OrderLogic, order_id: int, product_id: int) -> Order:
    return logic.add_product(order_id, product_id)
