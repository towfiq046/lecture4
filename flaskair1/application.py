from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:5504655@localhost/flaskair1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)    # tie this database with the flask app.

@app.route("/")     # default route. first page.
def index():
    flights = flightdb.query.all()     # equvalent to run a sql query.
    return render_template("index.html", flights = flights)   # passes the result to the index.html in for loop.

@app.route("/book", methods=["POST"])   # user info goes to book via post http post request method.
def book():
    """Book a flight"""

    # get form info what was typed in html form.
    name = request.form.get("name")
    try:
        flightID = int(request.form.get("flightID"))  # try to convert the value into int. maybe type cast.
    except ValueError:
        return render_template("error.html", message="Invald flight number.")  # sending value as string.

    # make sure flight exists.
    flight = flightdb.query.get(flightID)
    if flight is None:
        return render_template("error.html", message="No such flights.")

    # record the passenger and flight.
    passenger = passengerdb(name=name, flightID=flightID)
    db.session.add(passenger)
    db.session.commit()
    return render_template("success.html")

@app.route("/flights")
def flights():
    """list of all flights."""

    # from db select all the flights and send them to flights.html.
    flights = flightdb.query.all()
    return render_template("flights.html", flights=flights)

@app.route('/flights/<int:flightID>')
def flight(flightID):
    """details of a single flight."""

    flight = flightdb.query.get(flightID)
    if flight is None:
        return render_template("error.html", message="No such flight.")

    # get all the passengers.
    passengers = passengerdb.query.filter_by(flightID=flightID).all()    # all the rowes.
    return render_template("flight.html", flight=flight, passengers=passengers)
