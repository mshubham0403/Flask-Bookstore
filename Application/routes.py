from Application import app,db,login_required,login_user,logout_user,LoginManager
from flask_bcrypt import Bcrypt
from Application import schemas as sc
from flask import jsonify,request


@app.route("/")
def Home():
    return("Hello and Welcome to bookstore!")


@app.route("/add_book",methods=["POST"])
@login_required
def add_book():
    try:
        data =request.get_json()
        new_book =sc.Book(data)
        res =db.books.insertOne(new_book.to_dict())
        return jsonify({"message": "Book added successfully"}),200
    except Exception as e:
        return jsonify({"message": f"Failed to add book. Error: {str(e)}"}), 500
    

# Route to get all books
def get_books():
    books_data = list(db.books.find())
    books = [sc.Book.from_dict(book) for book in books_data]

    return jsonify({"books": [book.to_dict() for book in books]})

# Route to retrieve a specific book by ISBN
@app.route("/get_book/<isbn>", methods=["GET"])
@login_required
def get_book(isbn):
    book_data = db.books.find_one({"ISBN": isbn})

    if book_data:
        book = sc.Book.from_dict(book_data)
        return jsonify({"book": book.to_dict()})
    else:
        return jsonify({"message": "Book not found"}), 404

# Route to update book details
@app.route("/update_book/<isbn>", methods=["PUT"])
@login_required
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
@login_required
def delete_book(isbn):
    # Delete the book from the database
    result = db.books.delete_one({"ISBN": isbn})

    if result.deleted_count > 0:
        return jsonify({"message": "Book deleted successfully"})
    else:
        return jsonify({"message": "Book not found"}), 404
    
# ---------------- user and login routes-------------------




@app.route('/login', methods=['GET', 'POST'])
def login():
    data =request.get_json()
    # check if user exists
    userdata =db.user.find_one({"username":data["username"]})
    userdata =sc.User.from_dict(userdata)
    if userdata:
        try:
            if bcrypt.check_password_hash(userdata.password,data["password"]):
                login_user(userdata.username)
                return jsonify({"message": "login success"}),200
        except Exception as e:
            return jsonify({"message": f"Failed to add book. Error: {str(e)}"}), 500
    else:
        return jsonify({"message": "User not found"}), 404
   

#route to add user 

@app.route('/register', methods=['GET', 'POST'])
def register():
        # check if user already exists
        data =request.get_json()
        if not db.user.find_one({"username":data["username"]}):
            try:
                hashed_password=bcrypt.generate_password_hash(data["password"])
                new_user= sc.User(username=data["username"], password=hashed_password)
                db.user.insert_one(new_user.todict())
                
                return jsonify({"message": "user added successfully"}),200
            except Exception as e:
                return jsonify({"message": f"Failed to add user. Error: {str(e)}"}), 500
        else:
             return jsonify({"message": f"Failed user Exists."}), 409

    
#route to logout

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    try:
        logout_user()
        return jsonify({"message": f"user logged out."}), 200
    except Exception as e:
        return jsonify({"message": f"Failed to logout. Error: {str(e)}"}), 500

        

