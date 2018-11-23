from datetime import datetime
from typing import List, Optional, Tuple

import pytest

from bf_shop.entities import Client, Order, Product
from bf_shop.repositories import IClientRepository, IOrderRepository, IProductRepository

StaticRepositories = Tuple[IOrderRepository, IProductRepository, IClientRepository]


@pytest.fixture(scope="function")
def prepare_repositories() -> StaticRepositories:
    order = Order(id=1, created=datetime.now(), client=Client(id=1, name="John Doe"))

    product = Product(id=1, name="Test Product", price=100)

    class Orders(IOrderRepository):
        def create(self, client: Client) -> Order:
            ...

        def get(self, order_id: int) -> Order:
            return order

        def search(
            self, client: Optional[Client] = None, created: Optional[datetime] = None
        ) -> List[Order]:
            pass

    class Products(IProductRepository):
        def create(self, name: str, price: float) -> Product:
            ...

        def get(self, product_id: int) -> Product:
            return product

    class Clients(IClientRepository):
        def create(self, name: str) -> Client:
            ...

        def get(self, client_id: int) -> Client:
            ...

    return Orders(), Products(), Clients()
