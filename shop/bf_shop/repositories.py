import abc
from datetime import datetime
from typing import List, Optional

from bf_shop.entities import Client, Order, Product


class IClientRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, name: str) -> Client:
        pass

    @abc.abstractmethod
    def get(self, client_id: int) -> Client:
        pass


class IOrderRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, client: Client) -> Order:
        pass

    @abc.abstractmethod
    def get(self, order_id: int) -> Order:
        pass

    @abc.abstractmethod
    def search(
        self, client: Optional[Client] = None, created: Optional[datetime] = None
    ) -> List[Order]:
        pass


class IProductRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, name: str, price: float) -> Product:
        pass

    @abc.abstractmethod
    def get(self, product_id: int) -> Product:
        pass
