from flask import render_template, request, redirect, url_for
from glutenfree import app, db
from glutenfree.models import Starter, Main, Dessert, Drink


@app.route("/")
def home():
    return render_template("cuisine.html")


@app.route("/cuisine")
def cuisine():
    return render_template("cuisine.html")

@app.route("/starters")
def starters():
    starters = list(Starter.query.order_by(Starter.id).all())
    return render_template("starters.html", starters=starters)


@app.route("/add_cuisine")
def add_cuisine():
    return render_template("add_cuisine.html")




@app.route("/add_starters",  methods=["GET", "POST"])
def add_starters():
    if request.method == "POST":
        starter = Starter(
            starter_names=request.form.get("starter_names"),
            starter_tools=request.form.get("starter_tools"),
            starter_ingredients=request.form.get("starter_ingredients"),
            starter_directions=request.form.get("starter_directions")
        )
        db.session.add(starter)
        db.session.commit()
        return redirect(url_for("starters"))
    return render_template("add_starters.html" )







