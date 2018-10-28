from datetime import datetime
from typing import List, Optional

from bf_ram_db.ram_storage import RamStorage
from bf_shop.exceptions import OrderNotFound
from bf_shop.models import Client, Order
from bf_shop.providers import IOrderProvider


class OrderProvider(IOrderProvider):
    def __init__(self, static_data: Optional[List[Order]] = None) -> None:
        self._ram_storage = RamStorage[Order]()

        if static_data is None:
            static_data = []

        for order in static_data:
            self._ram_storage.add(order)

    def create(self, client: Client) -> Order:
        order_id = self._ram_storage.next_pk()

        self._ram_storage.add(Order(id=order_id, client=client, created=datetime.now()))

        return self._ram_storage.get(order_id)

    def get(self, order_id: int) -> Order:
        result = self._ram_storage.get(order_id)
        if result is None:
            raise OrderNotFound()
        return result

    def search(
        self, client: Optional[Client] = None, created: Optional[datetime] = None
    ) -> List[Order]:
        storage = self._ram_storage

        if client:
            storage = storage.search(client=client)

        if created:
            storage = storage.search(created=created)

        return storage.all()
