from typing import List, Optional

from bf_ram_db.ram_storage import RamStorage
from bf_shop.entities import Product
from bf_shop.exceptions import ProductNotFound
from bf_shop.repositories import IProductRepository


class ProductRepositories(IProductRepository):
    def __init__(self, static_data: Optional[List[Product]] = None) -> None:
        self._ram_storage = RamStorage[Product]()

        if static_data is None:
            static_data = []

        for product in static_data:
            self._ram_storage.add(product)

    def create(self, name: str, price: float) -> Product:
        product_id = self._ram_storage.next_pk()

        self._ram_storage.add(Product(id=product_id, name=name, price=price))

        return self._ram_storage.get(product_id)

    def get(self, product_id: int) -> Product:
        result = self._ram_storage.get(product_id)
        if result is None:
            raise ProductNotFound()
        return result
