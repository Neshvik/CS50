import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///dogs.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    """Show mainpage and options"""

    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return render_template("/indexafterlogin.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    else:
        # Extract the username and password from the form
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Require Username",400)
        elif not password:
            return apology("Require Password",400)
        elif not confirmation:
            return apology("Confirmation cannot be blank",400)
        elif password != confirmation:
            return apology("Passwords does not match",400)

        hash = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
            return render_template("/indexafterlogin.html")
        except:
            return apology("Username already exist",400)

@app.route("/addbreed", methods=["GET", "POST"])
@login_required
def addbreed():
    user_id = session["user_id"]

    if request.method == "GET":
        return render_template("addbreed.html")
    else:
        breed = request.form.get("breed")
        size = request.form.get("size")
        temperament = request.form.get("temperament")
        activitylevel = request.form.get("activitylevel")
        sheddinglevel = request.form.get("sheddinglevel")
        groomingneeds = request.form.get("groomingneeds")
        traininglevel = request.form.get("traininglevel")
        compatibilitywithchildren = request.form.get("compatibilitywithchildren")
        compatibilitywithotherpets = request.form.get("compatibilitywithotherpets")
        playspace = request.form.get("playspace")
        firsttimepawrents = request.form.get("firsttimepawrents")
        timealone = request.form.get("timealone")
        imageURL = request.form.get("imageURL")


        db.execute("INSERT INTO Dogs(Breed, Size, Temperament, ActivityLevel, SheddingLevel, GroomingNeeds, TrainingLevel, CompatibilityWithChildren, CompatibilityWithOtherPets, PlaySpace, FirstTimePawrents, timealone, ImageURL) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    breed, size, temperament, activitylevel, sheddinglevel, groomingneeds, traininglevel, compatibilitywithchildren, compatibilitywithotherpets, playspace, firsttimepawrents, timealone, imageURL)

        return render_template("/indexafterlogin.html")

@app.route("/indexafterlogin")
def indexafterlogin():
    return render_template("indexafterlogin.html")

@app.route("/traindog")
def traindog():
    return render_template("traindog.html")

@app.route("/buydogstuff")
def buydogstuff():
    return render_template("buydogstuff.html")

@app.route("/choosedog")
def choosedog():
    dogs = db.execute("SELECT * FROM Dogs")
    return render_template('choosedog.html', dogs=dogs)
