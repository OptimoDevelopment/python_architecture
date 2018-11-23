from typing import List

from injector import inject

from bf_shop.entities import Order
from bf_shop.repositories import IClientRepository, IOrderRepository, IProductRepository


class OrderLogic:
    @inject
    def __init__(
        self,
        orders: IOrderRepository,
        products: IProductRepository,
        clients: IClientRepository,
    ) -> None:
        self._orders: IOrderRepository = orders
        self._products: IProductRepository = products
        self._clients: IClientRepository = clients

    def search(self, client_id: int) -> List[Order]:
        client = self._clients.get(client_id)
        return self._orders.search(client)

    def create(self, client_id: int) -> Order:
        client = self._clients.get(client_id)
        return self._orders.create(client=client)

    def add_product(self, order_id: int, product_id: int) -> Order:
        order = self._orders.get(order_id)
        product = self._products.get(product_id)

        order.items.append(product)
        order.total_cost += product.price

        return order
