from flask import Flask
from Application import schemas as sc
from flask_pymongo import PyMongo
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config["SECRET_KEY"] = "db24c608640f5034b30b8e1e1eb5618ed0ffdbf5"
uri = "mongodb+srv://mshubham:Atlass2023@clusterh.ilp8ion.mongodb.net/Flask_bookstore?retryWrites=true&w=majority"
app.config["MONGO_URI"] = uri



bcrypt= Bcrypt(app)



login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view="login"
@login_manager.user_loader
def load_user(user_id):
    userdata =db.users.find_one({"usename": user_id})
    User_object =sc.User.from_dict(userdata)
    return User_object




# mongodb database
mongodb_client = PyMongo(app)
db = mongodb_client.db

from Application import routes
