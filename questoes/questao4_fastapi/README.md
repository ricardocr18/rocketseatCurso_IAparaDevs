# questao4_fastapi/README.md

# FastAPI Item Validation API

This project is a FastAPI application that provides an API for validating items with specific attributes. The API allows users to create and manage items, ensuring that the data adheres to defined constraints.

## Project Structure

```
questao4_fastapi
├── __init__.py
├── main.py
├── models.py
├── schemas.py
└── README.md
```

- **`__init__.py`**: Marks the directory as a Python package.
- **`main.py`**: Contains the main application logic and API endpoints.
- **`models.py`**: Defines the data models used in the application.
- **`schemas.py`**: Defines the Pydantic schemas for data validation and serialization.

## Installation

To run this application, you need to have Python and pip installed. You can install the required packages using the following command:

```bash
pip install fastapi[all] sqlalchemy
```

## Running the Application

To start the FastAPI application, navigate to the `questao4_fastapi` directory and run:

```bash
uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`.

## API Endpoints

- **POST /items/**: Create a new item.
- **GET /items/**: Retrieve all items.
- **GET /items/{item_id}**: Retrieve a specific item by ID.

## Data Model

Each item has the following attributes:

- **id**: A unique identifier for the item (UUID).
- **nome**: The name of the item (string, max 25 characters).
- **valor**: The value of the item (float, must be positive).
- **data**: The date associated with the item (date, cannot be in the future).

## License

This project is licensed under the MIT License.