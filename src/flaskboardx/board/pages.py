"""This module defines routes for handling static pages in the application.

It includes functions for rendering the home and the about page.
"""
import flask

bp = flask.Blueprint("pages", __name__)


@bp.route("/")
def home() -> str:
    """Render the home page.

    Returns:
        str: HTML content for the home page.
    """
    return flask.render_template("pages/home.html")


@bp.route("/about")
def about() -> str:
    """Render the about page.

    Returns:
        str: HTML content for the about page.
    """
    return flask.render_template("pages/about.html")
