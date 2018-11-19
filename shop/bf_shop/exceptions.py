from typing import Optional


class BaseException(Exception):
    def __init__(
        self, message: Optional[str] = None, detail: Optional[str] = None
    ) -> None:
        self.message = message or ""
        self.detail = detail or ""


class ElementNotFound(BaseException):
    NOT_FOUND = "Element not found"
    DETAILS = ""

    def __init__(self) -> None:
        super().__init__(message=self.NOT_FOUND, detail=self.DETAILS)


class ClientNotFound(ElementNotFound):
    DETAILS = "Client not found"


class ProductNotFound(ElementNotFound):
    DETAILS = "Product not found"


class OrderNotFound(ElementNotFound):
    DETAILS = "Order not found"
