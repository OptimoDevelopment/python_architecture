from typing import List

from injector import inject

from bf_shop.entities import Order
from bf_shop.providers import IClientProvider, IOrderProvider, IProductProvider


class OrderLogic:
    @inject
    def __init__(
        self,
        order_provider: IOrderProvider,
        product_provider: IProductProvider,
        client_provider: IClientProvider,
    ) -> None:
        self._order_provider: IOrderProvider = order_provider
        self._product_provider: IProductProvider = product_provider
        self._client_provider: IClientProvider = client_provider

    def search(self, client_id: int) -> List[Order]:
        client = self._client_provider.get(client_id)
        return self._order_provider.search(client)

    def create(self, client_id: int) -> Order:
        client = self._client_provider.get(client_id)
        return self._order_provider.create(client=client)

    def add_product(self, order_id: int, product_id: int) -> Order:
        order = self._order_provider.get(order_id)
        product = self._product_provider.get(product_id)

        order.items.append(product)
        order.total_cost += product.price

        return order
