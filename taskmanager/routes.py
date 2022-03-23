from flask import render_template, request, redirect, url_for
from taskmanager import app, db
# importing the table classes to generate the db
from taskmanager.models import Category, Task


# THE VIEWS - FUNCTIONS WHICH LINK TO TEMPLATED PAGES
# home view function (the task page)
@app.route("/")
def home():
    return render_template("tasks.html")


# finds the asociated file, is called by the function name, renders the template
@app.route("/categories")
def categories():
    return render_template("categories.html")


# need to specify the methods since we will be submitting a form
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # adding the POST functionality
    if request.method == "POST":
        # creates new instance of the Category class
        category = Category(category_name=request.form.get("category_name"))
        # opens a session to save and commit it
        db.session.add(category)
        db.session.commit()
        # returns the user to the catergories page
        return redirect(url_for("categories"))
    # rendered when add_category button is clicked (GET method)
    return render_template("add_category.html")
