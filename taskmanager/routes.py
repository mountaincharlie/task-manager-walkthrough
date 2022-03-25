from flask import render_template, request, redirect, url_for
from taskmanager import app, db
# importing the table classes to generate the db
from taskmanager.models import Category, Task


# THE VIEWS - FUNCTIONS WHICH LINK TO TEMPLATED PAGES
# home view function (the task page)
@app.route("/")
def home():
    # querying the db for a cursor obj, converted to list, to populate the page
    tasks = list(Task.query.order_by(Task.due_date).all())
    # variables needed in the html page need to be passed in here (var_page=var_here)
    return render_template("tasks.html", tasks=tasks)


# finds the asociated file, is called by the function name, renders the template
@app.route("/categories")
def categories():
    # querying the db for a cursor obj, converted to list, to populate the page
    categories = list(Category.query.order_by(Category.category_name).all())
    # variables needed in the html page need to be passed in here (var_page=var_here)
    return render_template("categories.html", categories=categories)


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


# vars being passed back into python functions must be in <>
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    # making edits
    if request.method == "POST":
        # renaming on the db and taking back to the cat page
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)  # getting the item
    db.session.delete(category)  # deleting it
    db.session.commit()  # commiting the changes
    return redirect(url_for("categories"))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    # getting a list of all categories
    categories = list(Category.query.order_by(Category.category_name).all())
    # adding the POST functionality
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")
        )
        db.session.add(task)
        db.session.commit()
        # returns the user to the catergories page
        return redirect(url_for("home"))
    # rendered when add_category button is clicked (GET method)
    return render_template("add_task.html", categories=categories)


# vars being passed back into python functions must be in <>
@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    # making edits
    if request.method == "POST":
        # all fields here so if some arent edited, they dont delete
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.is_urgent = bool(True if request.form.get("is_urgent") else False)
        task.due_date = request.form.get("due_date")
        task.category_id = request.form.get("category_id")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_task.html", task=task, categories=categories)


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)  # getting the item
    db.session.delete(task)  # deleting it
    db.session.commit()  # commiting the changes
    return redirect(url_for("home"))
