# Bookstore API

**Description:**

This Flask application provides a RESTful API for managing a bookstore. It allows users to add, retrieve, update, and delete books, as well as register and login.

**Endpoints:**

**Books**

* **GET /books** - Get all books
* **POST /add_book** - Add a new book
* **GET /get_book/<isbn>** - Get a book by ISBN
* **PUT /update_book/<isbn>** - Update a book by ISBN
* **DELETE /delete_book/<isbn>** - Delete a book by ISBN

**Users**

* **POST /register** - Register a new user
* **POST /login** - Login a user
* **GET /logout** - Logout a user

**Usage:**

1. Clone the repository:

```
git clone https://github.com/mshubham0203/flask-bookstore.git
```

2. Install the required Python packages:

```
pip install -r requirements.txt
```

3. Create a `.env` file in the project directory and add the following environment variables:

```
MONGO_URI=<mongodb connection string>
SECRET_KEY=<secret key for Flask session>
```

4. Run the application:

```
flask run
```

5. Open Postman or another API testing tool and send requests to the API endpoints.

**Example:**

To add a new book, send a POST request to the `/add_book` endpoint with the following JSON payload:

```
{
  "title": "The Hitchhiker's Guide to the Galaxy",
  "author": "Douglas Adams",
  "ISBN": "978034537",
  "price": 1299,
  "quantity": 5
}
```

You should receive a response like this:

```
{
  "message": "Book added successfully"
}
```

To get all books, send a GET request to the `/books` endpoint. You should receive a response like this:

```
{
  "books": [
    {
      "book_id": 1,
      "title": "The Hitchhiker's Guide to the Galaxy",
      "author": "Douglas Adams",
      "ISBN": "9780345397",
      "price": 1299,
      "quantity": 5
    }
  ]
}
```

