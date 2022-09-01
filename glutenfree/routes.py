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
    return render_template("add_starters.html")


@app.route("/edit_starters/<int:starter_id>",  methods=["GET", "POST"])
def edit_starters(starter_id):
    starter = Starter.query.get_or_404(starter_id)
    if request.method == "POST":
        starter.starter_names = request.form.get("starter_names"),
        starter.starter_tools = request.form.get("starter_tools"),
        starter.starter_ingredients = request.form.get("starter_ingredients"),
        starter.starter_directions = request.form.get("starter_directions")
        db.session.commit()
        return redirect(url_for("starters"))
    return render_template("edit_starters.html", starter=starter)


@app.route("/delete_starters/<int:starter_id>")
def delete_starters(starter_id):
    starter = Starter.query.get_or_404(starter_id)
    db.session.delete(starter)
    db.session.commit()
    return redirect(url_for("starters"))


@app.route("/mains")
def mains():
    mains= list(Main.query.order_by(Main.id).all())
    return render_template("mains.html", mains=mains)


@app.route("/add_mains",  methods=["GET", "POST"])
def add_mains():
    if request.method == "POST":
        main = Main(
            main_names=request.form.get("main_names"),
            main_tools=request.form.get("main_tools"),
            main_ingredients=request.form.get("main_ingredients"),
            main_directions=request.form.get("main_directions")
        )
        db.session.add(main)
        db.session.commit()
        return redirect(url_for("mains"))
    return render_template("add_mains.html")


@app.route("/edit_mains/<int:main_id>",  methods=["GET", "POST"])
def edit_mains(main_id):
    main = Main.query.get_or_404(main_id)
    if request.method == "POST":
        main.main_names = request.form.get("main_names"),
        main.main_tools = request.form.get("main_tools"),
        main.main_ingredients = request.form.get("main_ingredients"),
        main.main_directions = request.form.get("main_directions")
        db.session.commit()
        return redirect(url_for("mains"))
    return render_template("edit_mains.html", main=main)