from Application import app,db
from Application import schemas as sc
from flask import jsonify,request

@app.route("/")
def Home():
    return("Hello and Welcome to bookstore!")
@app.route("/add_book",methods=["POST"])
def add_book():
    try:
        data =request.get_json()
        new_book =sc.Book(data)
        res =db.books.insertOne(new_book.to_dict())
        return jsonify({"message": "Book added successfully"}),200
    except Exception as e:
        return jsonify({"message": f"Failed to add book. Error: {str(e)}"}), 500
@app.route("/add_user",methods=["POST"])
def add_user():
    try:
        data =request.get_json()
        username =data["username"]
        pwd =data["password"]
        email =data["email"]
        new_user =sc.User(username,pwd,email)
        res =db.user.insert_one(new_user.to_dict())
        return jsonify({"message": "user added successfully"}),200
    except Exception as e:
        return jsonify({"message": f"Failed to add user. Error: {str(e)}"}), 500
# Route to get all books
def get_books():
    books_data = list(db.books.find())
    books = [sc.Book.from_dict(book) for book in books_data]

    return jsonify({"books": [book.to_dict() for book in books]})

# Route to retrieve a specific book by ISBN
@app.route("/get_book/<isbn>", methods=["GET"])
def get_book(isbn):
    book_data = db.books.find_one({"ISBN": isbn})

    if book_data:
        book = sc.Book.from_dict(book_data)
        return jsonify({"book": book.to_dict()})
    else:
        return jsonify({"message": "Book not found"}), 404

# Route to update book details
@app.route("/update_book/<isbn>", methods=["PUT"])
def update_book(isbn):
    data = request.get_json()

    # Update book details in the database
    result = db.books.update_one({"ISBN": isbn}, {"$set": data})

    if result.modified_count > 0:
        return jsonify({"message": "Book updated successfully"})
    else:
        return jsonify({"message": "Book not found or no changes made"}), 404

# Route to delete a book
@app.route("/delete_book/<isbn>", methods=["DELETE"])
def delete_book(isbn):
    # Delete the book from the database
    result = db.books.delete_one({"ISBN": isbn})

    if result.deleted_count > 0:
        return jsonify({"message": "Book deleted successfully"})
    else:
        return jsonify({"message": "Book not found"}), 404

