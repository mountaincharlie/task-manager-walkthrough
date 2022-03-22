from flask import render_template
from taskmanager import app, db
# importing the table classes to generate the db
from taskmanager.models import Category, Task


# home view
@app.route("/")
def home():
    return render_template("base.html")
