import logging
import connexion
from tensorhive.config import API_CONFIG
from tensorhive.database import db_session
log = logging.getLogger(__name__)


class APIServer():
    def start(self):
        app = connexion.FlaskApp(__name__)
        log.info(
            'API docs (Swagger UI) available at: http://<address>:<port>/v1.0/ui/')

        @app.app.teardown_appcontext
        def shutdown_session(exception=None):
            db_session.remove()

        app.add_api(API_CONFIG.SPECIFICATION_FILE,
                    arguments={'title': API_CONFIG.TITLE},
                    resolver=connexion.RestyResolver('tensorhive.api.api'))
        app.run(server=API_CONFIG.SERVER_BACKEND,
                port=API_CONFIG.SERVER_PORT,
                debug=API_CONFIG.SERVER_DEBUG)


if __name__ == '__main__':
    APIServer().start()
