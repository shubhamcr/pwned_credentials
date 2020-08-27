from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

bootstrap = Bootstrap()


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    bootstrap.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.breaches import breaches_bp
    app.register_blueprint(breaches_bp)

    return app