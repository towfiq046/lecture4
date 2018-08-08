import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class flightdb(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    # used to access the info about the related fields using       keyword.
    passengersRelation = db.relationship("passengerdb", backref = "flightdb", lazy = True)
    # connects multiple tables.            keyword

    def addPassenger(self, name):   # line 36 in flask app.
        newPassenger = passengerdb(name = name, flightID = self.id)   # self refers to the flight model.
        db.session.add(newPassenger)
        db.session.commit()

class passengerdb(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flightID = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
