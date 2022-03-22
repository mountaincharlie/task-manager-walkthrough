from flask import render_template
from taskmanager import app, db
# importing the table classes to generate the db
from taskmanager.models import Category, Task


# home view function (the task page)
@app.route("/")
def home():
    return render_template("tasks.html")
