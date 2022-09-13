from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plateNumber = db.Column(db.String(150), unique=True, nullable=False)
    engineNumber = db.Column(db.String(150),unique=True, nullable=True)
    ownerName = db.Column(db.String(150))
    ownerContact = db.Column(db.String(150))
    lastSeenLoc = db.Column(db.String(150))
    lastSeenDate = db.Column(db.DateTime)
    isHotplate = db.Column(db.Boolean, default=False)



class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    notifyIfFoundHotPlate = db.Column(db.Boolean, default=False)
    adminContact = db.Column(db.String(150))



# class Violation(db.model):
#     pass
