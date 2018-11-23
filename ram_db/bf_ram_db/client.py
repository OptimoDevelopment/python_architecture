from typing import List, Optional

from bf_ram_db.ram_storage import RamStorage
from bf_shop.exceptions import ClientNotFound
from bf_shop.entities import Client
from bf_shop.providers import IClientProvider


class ClientProvider(IClientProvider):
    def __init__(self, static_data: Optional[List[Client]] = None) -> None:
        self._ram_storage = RamStorage[Client]()

        if static_data is None:
            static_data = []

        for client in static_data:
            self._ram_storage.add(client)

    def create(self, name: str) -> Client:
        client_id = self._ram_storage.next_pk()

        self._ram_storage.add(Client(id=client_id, name=name))

        return self._ram_storage.get(client_id)

    def get(self, client_id: int) -> Client:
        result = self._ram_storage.get(client_id)
        if result is None:
            raise ClientNotFound()

        return result
