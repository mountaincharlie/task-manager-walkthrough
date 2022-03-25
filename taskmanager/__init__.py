import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# linking only found env.py file (since its never pushed to github)
if os.path.exists("env.py"):
    import env  # noqa


# creating an instance of the imported Flask class
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# if we are working in dev mode, we want the locally hosted db
if os.environ.get("DEVELOPMENT") == True:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:  # otherwise we want Heroku's one
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

# creating instance of the imported SQLAlchemy class
db = SQLAlchemy(app)

from taskmanager import routes  # noqa
