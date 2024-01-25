from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "db24c608640f5034b30b8e1e1eb5618ed0ffdbf5"
uri = "mongodb+srv://mshubham:Atlass2023@clusterh.ilp8ion.mongodb.net/Flask_bookstore?retryWrites=true&w=majority"
app.config["MONGO_URI"] = uri

# mongodb database
mongodb_client = PyMongo(app)
db = mongodb_client.db

from Application import routes
