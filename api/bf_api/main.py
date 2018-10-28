import connexion
import flask
from connexion.apis.flask_api import FlaskApi
from flask_injector import FlaskInjector

from bf_api.encoders import ApiJsonEncoder
from bf_api.injections import LogicModule, MemoryProvidersModule
from bf_shop.exceptions import ElementNotFound


def main() -> None:
    app = connexion.FlaskApp(__name__, specification_dir="swagger/")
    app.add_api("api.yaml")

    @app.app.errorhandler(ElementNotFound)
    def handle_offer_mgr_exception(exc) -> flask.Response:
        response = connexion.problem(status=400, title=exc.message, detail=exc.detail)

        return FlaskApi.get_response(response)

    flask_injector = FlaskInjector(
        app=app.app, modules=[LogicModule, MemoryProvidersModule]
    )
    app.app.config["FLASK_INJECTOR"] = flask_injector

    app.app.json_encoder = ApiJsonEncoder
    app.run(port=8080, debug=True)


if __name__ == "__main__":
    main()
