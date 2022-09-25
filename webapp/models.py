from . import db
from flask_login import UserMixin
from datetime import datetime
now = datetime.now()
now = datetime.strftime(now,"%Y-%m-%dT%H:%M")
now = datetime.strptime(now,"%Y-%m-%dT%H:%M")



class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plateNumber = db.Column(db.String(150), unique=True, nullable=False)
    engineNumber = db.Column(db.String(150),unique=True, nullable=True)
    ownerName = db.Column(db.String(150))
    ownerContact = db.Column(db.String(150))
    lastSeenLoc = db.Column(db.String(150))
    lastSeenDate = db.Column(db.DateTime)
    isHotplate = db.Column(db.Boolean, default=False)
    violations = db.relationship('Violation')



class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    notifyIfFoundHotPlate = db.Column(db.Boolean, default=False)
    adminContact = db.Column(db.String(150))
    createdViolations = db.relationship('Violation')



class Violation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    violationName = db.Column(db.String(200), nullable=False)
    violationDesc = db.Column(db.String(5000), nullable=False)
    violationOwner = db.Column(db.Integer, db.ForeignKey('car.id'))
    violationAddedBy = db.Column(db.Integer, db.ForeignKey('admin.id'))
    createdAt = db.Column(db.DateTime, default=now)
    isResolved = db.Column(db.Boolean, default=False)
    resolvedDate = db.Column(db.DateTime)
