from functools import reduce
from typing import Any, Dict, Generic, List, Optional, TypeVar

T = TypeVar("T")
StorageType = Dict[int, T]


class RamStorage(Generic[T]):
    def __init__(self, storage: StorageType = None, pk_name: str = "id") -> None:
        self._pk_name: str = pk_name
        self._max_pk: int = 0
        if storage is None:
            storage = {}
        self._storage: StorageType = storage

    def add(self, item: T) -> None:
        item_pk = self._get_item_pk(item)
        self._storage[item_pk] = item
        self._max_pk = max(item_pk, self._max_pk)

    def get(self, pk: int) -> Optional[T]:
        return self._storage[pk] if pk in self._storage else None

    def search(self, **kwargs: Any) -> "RamStorage[T]":
        def filter_by(storage, current_filter: tuple) -> StorageType:
            return {
                k: v
                for k, v in storage.items()
                if getattr(v, current_filter[0]) == current_filter[1]
            }

        storage = reduce(
            filter_by, [self._storage] + [(k, v) for k, v in kwargs.items()]
        )
        return RamStorage(storage)

    def remove(self, item: T) -> None:
        pk = self._get_item_pk(item)
        if pk in self._storage:
            del (self._storage[pk])

    def all(self) -> List[T]:
        return list(self._storage.values())

    def _get_item_pk(self, item: T) -> int:
        return getattr(item, self._pk_name)

    def next_pk(self) -> int:
        self._max_pk += 1
        return self._max_pk
