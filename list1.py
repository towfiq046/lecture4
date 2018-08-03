import os

from flask import Flask
from models import *

# flask configaration with db.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:5504655@localhost/lecture4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def main():
    allFlights = Flight.query.all()
    for flight in allFlights:
        print(f'{flight.origin} to {flight.destination}, {flight.duration} minutes')


if __name__ == '__main__':
    with app.app_context(): # to find the right application context was introduced.
        main()
