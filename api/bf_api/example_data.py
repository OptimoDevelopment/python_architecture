from datetime import datetime

from bf_shop.models import Client, Order, Product

clients = [
    Client(id=1, name="Angelina Jolie"),
    Client(id=2, name="John Doe")
]

products = [
    Product(id=1, name="Phone", price=999),
    Product(id=2, name="RTX 2080 Ti", price=5499),
]

orders = [Order(id=1, created=datetime.now(), client=clients[0], total_cost=0)]
