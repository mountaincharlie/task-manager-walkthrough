from flask import render_template
from taskmanager import app, db


# home view
@app.route("/")
def home():
    return render_template("base.html")
