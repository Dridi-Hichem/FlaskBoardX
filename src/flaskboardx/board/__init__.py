"""This package defines a Flask application for managing posts & static pages.

It includes modules for database handling, page rendering, and post
management.

The package also loads environment variables from a `.env` file
and configures the Flask application.
"""

import os
import flask
from dotenv import load_dotenv

from . import database, errors, pages, posts

# load environment variables from the `.env` file
# into the application's environment
load_dotenv()


def create_app() -> flask.Flask:
    """Create and configure the Flask application instance.

    Returns:
        flask.Flask: An instance of the Flask application.
    """
    app = flask.Flask(__name__)
    app.config.from_prefixed_env()
    app.logger.setLevel("INFO")

    # Initialize the database integration into the app
    database.init_app(app)

    # Register blueprints for pages, posts and errors
    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    app.register_error_handler(404, errors.page_not_found)

    # Log environment information for debugging purposes
    app.logger.debug(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    app.logger.debug(f"Using Database: {app.config.get('DATABASE')}")

    return app
