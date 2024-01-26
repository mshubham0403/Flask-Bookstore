# Define the Book schema
class Book:
    def __init__(self, id,title, author, ISBN, price, quantity):
        self.book_id = id
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.price = price
        self.quantity = quantity

    def to_dict(self):

        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "ISBN": self.ISBN,
            "price": self.price,
            "quantity": self.quantity
        }
    @classmethod
    def from_dict(cls, data):
        
        try:
            bookObject =cls(
                book_id=data["book_id"],
                title=data["title"],
                author=data["author"],
                ISBN=data["ISBN"],
                price=data["price"],
                quantity=data["quantity"]
            )
            return bookObject
        except Exception as e:
            return None
class User:
    def __init__(self,username,pwd,email):
        self.username = username
        self.password = pwd
        self.email = email
        

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        
        try :
            userObject =cls(
                username=data["username"],
                email=data["email"],
                password=data["password"]
             )
            return userObject
        except Exception as e:
            return None
            


        