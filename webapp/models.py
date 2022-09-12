from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# class Vehicle(db.Model):
#     pass


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    notifyIfFoundHotPlate = db.Column(db.Boolean, default=False)
    adminContact = db.Column(db.String(150))

# Admin(LTO-Officer)
#     id: Int (Unique, Primary Key)
#     email: String(required, unique)
#     password: String
#     name: String
#     notifyIfFoundHotPlate: Boolean(default: False)
#     adminContact: String(unique)


# class Violation(db.model):
#     pass
