#using flask to insert without explicitly writing sql command.

import csv, os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:5504655@localhost/flaskair1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def main():
    f = open('flights.csv')
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        flight = flightdb(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)
        print(f'Added flight from {origin} to {destination} lasting {duration} minutes.')
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        main()
