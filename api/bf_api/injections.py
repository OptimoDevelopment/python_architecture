import injector

from bf_shop.repositories import IClientRepository, IOrderRepository, IProductRepository


class LogicModule(injector.Module):
    def configure(self, binder: injector.Binder) -> None:
        from bf_shop.logic import OrderLogic

        binder.bind(OrderLogic, to=OrderLogic, scope=injector.SingletonScope)


class MemoryProvidersModule(injector.Module):
    @injector.singleton
    @injector.provider
    def provide_clients(self) -> IClientRepository:
        from bf_ram_db.client import ClientRepositories
        from bf_api.example_data import clients

        return ClientRepositories(static_data=clients)

    @injector.singleton
    @injector.provider
    def provide_orders(self) -> IOrderRepository:
        from bf_ram_db.order import OrderRepositories
        from bf_api.example_data import orders

        return OrderRepositories(static_data=orders)

    @injector.singleton
    @injector.provider
    def provide_products(self) -> IProductRepository:
        from bf_ram_db.product import ProductRepositories
        from bf_api.example_data import products

        return ProductRepositories(static_data=products)
