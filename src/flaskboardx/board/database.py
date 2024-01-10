"""Database Functionalities.

This module provides functionality for database initialization, connection
management, and closing in a Flask application.

It includes a CLI command for initializing the database, a function
to integrate the command into the app, and functions for obtaining
and closing database connections.
"""

import sqlite3

import click
import flask


def init_app(app: flask.Flask) -> None:
    """Integrate a database initialization command into the application's CLI.

    Args:
        app (flask.Flask): The Flask aplication instance.
    """
    app.teardown_appcontext(close_db)  # register close_db() to the app
    app.cli.add_command(init_db_command)


@click.command("init-db")
def init_db_command() -> None:
    """Define the core logic for database initialization."""
    db = get_db()

    with flask.current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))

    click.echo("You successfully initialized the database!")


def get_db() -> sqlite3.Connection:
    """Return a databse connection.

    Either return an existing connection or establish a new one first.

    Returns:
        sqlite3.Connection: The databse connection.
    """
    if "db" not in flask.g:
        flask.g.db = sqlite3.connect(
            flask.current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )

        # Allows to access the column by name, user can interact with
        # the database similarly to interacting with a dictionary
        flask.g.db.row_factory = sqlite3.Row

    return flask.g.db


def close_db(e=None) -> None:
    """Close the database connection.

    Args:
        e (Exception): An error for error-specific handling.
    """
    db = flask.g.pop("db", None)

    if db is not None:
        db.close()
