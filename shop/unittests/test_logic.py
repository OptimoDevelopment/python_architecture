from unittests.conftest import StaticRepositories


def test_add_product_increase_orders_total_cost(
    prepare_repositories: StaticRepositories
) -> None:
    from bf_shop.logic import OrderLogic

    orders, products, clients = prepare_repositories
    order = orders.get(1)
    logic = OrderLogic(orders=orders, products=products, clients=clients)

    assert order.total_cost == 0

    logic.add_product(order_id=1, product_id=1)

    assert order.total_cost == 100
