from flask import render_template, request, redirect, url_for, Blueprint
from glutenfree import app, db
from glutenfree.models import Starter, Main, Dessert, Drink, User


main = Blueprint('main', __name__)


@app.route("/")
def home():
    # home page
    return render_template("cuisine.html")


@app.route("/cuisine")
def cuisine():
    # render cuisine as home page
    return render_template("cuisine.html")


@app.route("/starters")
def starters():
    # starters page
    starters = list(Starter.query.order_by(Starter.id).all())
    return render_template("starters.html", starters=starters)


@app.route("/add_starters",  methods=["GET", "POST"])
def add_starters():
    # starters to the database
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
    # add starters in the database
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
    # delete starters in the database
    starter = Starter.query.get_or_404(starter_id)
    db.session.delete(starter)
    db.session.commit()
    return redirect(url_for("starters"))


@app.route("/mains")
def mains():
    # Main course to the database
    mains = list(Main.query.order_by(Main.id).all())
    return render_template("mains.html", mains=mains)


@app.route("/add_mains",  methods=["GET", "POST"])
def add_mains():
    # add Main Course to the database
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
    # add Main Course from the database
    main = Main.query.get_or_404(main_id)
    if request.method == "POST":
        main.main_names = request.form.get("main_names"),
        main.main_tools = request.form.get("main_tools"),
        main.main_ingredients = request.form.get("main_ingredients"),
        main.main_directions = request.form.get("main_directions")
        db.session.commit()
        return redirect(url_for("mains"))
    return render_template("edit_mains.html", main=main)


@app.route("/delete_mains/<int:main_id>")
def delete_mains(main_id):
    # delete Main course from the database
    main = Main.query.get_or_404(main_id)
    db.session.delete(main)
    db.session.commit()
    return redirect(url_for("mains"))


@app.route("/desserts")
def desserts():
    # desserts to the database
    desserts = list(Dessert.query.order_by(Dessert.id).all())
    return render_template("desserts.html", desserts=desserts)


@app.route("/add_desserts",  methods=["GET", "POST"])
def add_desserts():
    # add desserts to the database
    if request.method == "POST":
        dessert = Dessert(
            dessert_names=request.form.get("dessert_names"),
            dessert_tools=request.form.get("dessert_tools"),
            dessert_ingredients=request.form.get("dessert_ingredients"),
            dessert_directions=request.form.get("dessert_directions")
        )
        db.session.add(dessert)
        db.session.commit()
        return redirect(url_for("desserts"))
    return render_template("add_desserts.html")


@app.route("/edit_desserts/<int:dessert_id>",  methods=["GET", "POST"])
def edit_desserts(dessert_id):
    # edit desserts in the database
    dessert = Dessert.query.get_or_404(dessert_id)
    if request.method == "POST":
        dessert.dessert_names = request.form.get("dessert_names"),
        dessert.dessert_tools = request.form.get("dessert_tools"),
        dessert.dessert_ingredients = request.form.get("dessert_ingredients"),
        dessert.dessert_directions = request.form.get("dessert_directions")
        db.session.commit()
        return redirect(url_for("desserts"))
    return render_template("edit_desserts.html", dessert=dessert)


@app.route("/delete_desserts/<int:dessert_id>")
def delete_desserts(dessert_id):
    # delete desserts in the database
    dessert = Dessert.query.get_or_404(dessert_id)
    db.session.delete(dessert)
    db.session.commit()
    return redirect(url_for("desserts"))


@app.route("/drinks")
def drinks():
    # drinks to the database
    drinks = list(Drink.query.order_by(Drink.id).all())
    return render_template("drinks.html", drinks=drinks)


@app.route("/add_drinks",  methods=["GET", "POST"])
def add_drinks():
    # add drinks to the database
    if request.method == "POST":
        drink = Drink(
            drink_names=request.form.get("drink_names"),
            drink_tools=request.form.get("drink_tools"),
            drink_ingredients=request.form.get("drink_ingredients"),
            drink_directions=request.form.get("drink_directions")
        )
        db.session.add(drink)
        db.session.commit()
        return redirect(url_for("drinks"))
    return render_template("add_drinks.html")


@app.route("/edit_drinks/<int:drink_id>",  methods=["GET", "POST"])
def edit_drinks(drink_id):
    # edit drinks in the database
    drink = Drink.query.get_or_404(drink_id)
    if request.method == "POST":
        drink.drink_names = request.form.get("drink_names"),
        drink.drink_tools = request.form.get("drink_tools"),
        drink.drink_ingredients = request.form.get("drink_ingredients"),
        drink.drink_directions = request.form.get("drink_directions")
        db.session.commit()
        return redirect(url_for("drinks"))
    return render_template("edit_drinks.html", drink=drink)
