"""This module defines routes for handling posts in the application.

It includes functions for creating new posts and displaying a list
of existing posts.
"""

import flask

from . import database

bp = flask.Blueprint("posts", __name__)


@bp.route("/create", methods=("Get", "POST"))
def create() -> flask.Response | str:
    """Create a new post.

    Note:
        - If the request method is `POST`, extracts author and message
            from the form data. Inserts the post into the database
            and redirects to the list of posts.
        - If the request is `Get`, renders the `create.html` template
            for creating a new post.

    Returns:
        flask.Response: A response object or HTML content.
    """
    if flask.request.method == "POST":
        author = flask.request.form["author"] or "Anonymous"
        message = flask.request.form["message"]

        if message:
            db = database.get_db()
            db.execute(
                "INSERT INTO post (author, message) VALUES (?, ?)",
                (author, message),
            )
            db.commit()

            flask.current_app.logger.info(f"New post by {author}")
            flask.flash(f"Thanks for posting, {author}", category="success")

            return flask.redirect(flask.url_for("posts.posts"))

        flask.flash("You need to post a message.", category="error")

    return flask.render_template("posts/create.html")


@bp.route("/posts")
def posts() -> str:
    """Display a list of posts.

    Steps:
        1. Retrieves posts from the database, ordered be creation date
            in descending order.
        2. Renders the `posts.html` template with the retrieved posts.

    Returns:
        str: HTML content displaying a list of posts.
    """
    db = database.get_db()
    all_posts = db.execute(
        "SELECT author, message, created FROM post ORDER BY created DESC"
    ).fetchall()

    return flask.render_template("posts/posts.html", posts=all_posts)
