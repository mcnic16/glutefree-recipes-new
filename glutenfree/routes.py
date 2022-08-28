from flask import render_template
from glutenfree import app, db
from glutenfree import Category, Task


@app.route("/")
def home():
    return render_template("base.html")