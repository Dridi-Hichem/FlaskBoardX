"""Custom errors.

This module defines a custom error handling function for handling 404 Not
Found errors in the application.

Functions:
    - `page_not_found`: Custom error handler for 404 Not Found errors.
        Logs error details and renders a custom 404 error page.
"""
from __future__ import annotations

import typing

import flask


if typing.TYPE_CHECKING:
    from werkzeug.exceptions import HTTPException as werkzeug_HTTPException


def page_not_found(e: werkzeug_HTTPException) -> str:
    """Render a custom error handler for 404 Not Found errors.

    Logs information about the error, including the error name, code, and URL,
    and renders a custom 404 error page.

    Args:
        e (werkzeug.exceptions.HTTPException): The exception object
            representing the 404 Not Found error.

    Returns:
        str: HTML content of the rendered 404 error page.
    """
    flask.current_app.logger.info(f"'{e.name}' error ({e.code}) at {flask.request.url}")

    return flask.render_template("errors/404.html")
