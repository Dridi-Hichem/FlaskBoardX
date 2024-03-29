# FlaskBoardX

FlaskBoardX is a simple Flask web application for managing posts and static pages. It provides a basic structure for a web board where users can create posts, view a list of posts, and explore static pages.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/FlaskBoardX.git
    cd FlaskBoardX
    ```

2. Install dependencies using Poetry:

    ```bash
    poetry install
    ```

3. Create a `.env` file based on the provided template:

    ```bash
    cp .env_template .env
    ```

   Edit the `.env` file to set your specific configuration, especially the `FLASK_SECRET_KEY`.

4. Initialize the database:

    ```bash
    poetry run python -m flask --app flask_board_x.board init-db
    ```

5. Run the server:

    ```bash
    poetry run python -m flask --app flask_board_x.board run --port 8000 --debug
    ```

   Optionally, you can use the `--debug` flag for development.

6. Visit [http://localhost:8000](http://localhost:8000) in your web browser to interact with the app.
