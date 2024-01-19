from flask import Flask
import os
from dotenv import load_dotenv
import secrets

from board import requirement,database,intake,home

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.secret_key = secrets.token_hex(16)
    app.config.from_prefixed_env()

    database.init_app(app)

    app.register_blueprint(requirement.bp)
    app.register_blueprint(intake.bp)
    app.register_blueprint(home.bp)
    return app

