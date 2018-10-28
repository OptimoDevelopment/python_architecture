import injector

from bf_shop.providers import IClientProvider, IOrderProvider, IProductProvider


class LogicModule(injector.Module):
    def configure(self, binder: injector.Binder) -> None:
        from bf_shop.logic import OrderLogic

        binder.bind(OrderLogic, to=OrderLogic, scope=injector.SingletonScope)


class MemoryProvidersModule(injector.Module):
    @injector.singleton
    @injector.provider
    def provide_clients(self) -> IClientProvider:
        from bf_ram_db.client import ClientProvider
        from bf_api.example_data import clients

        return ClientProvider(static_data=clients)

    @injector.singleton
    @injector.provider
    def provide_orders(self) -> IOrderProvider:
        from bf_ram_db.order import OrderProvider
        from bf_api.example_data import orders

        return OrderProvider(static_data=orders)

    @injector.singleton
    @injector.provider
    def provide_products(self) -> IProductProvider:
        from bf_ram_db.product import ProductProvider
        from bf_api.example_data import products

        return ProductProvider(static_data=products)
