import os
from .routes import register_blueprints
from flask import Flask
from .extensions import db, migrate


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://myuser:your_strong_password@localhost:5432/pc-build-part-ranker"

    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_pre_ping": True,
    }

    db.init_app(app)
    migrate.init_app(app, db)

    # Register models with SQLAlchemy
    from . import models
    register_blueprints(app)
    return app
