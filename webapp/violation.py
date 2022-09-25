from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Violation, Car, Admin
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime
now = datetime.now()
now = datetime.strftime(now,"%Y-%m-%dT%H:%M")
now = datetime.strptime(now,"%Y-%m-%dT%H:%M")


violationBlueprint = Blueprint('violation', __name__)

@violationBlueprint.route('add', methods=['GET', 'POST'])
@login_required
def addViolation():
    car_id = request.args.get('id')
    car = Car.query.filter_by(id=car_id).first()
    if request.method == "POST":
        violationName = request.form.get('violationName')
        violationDesc = request.form.get('violationDesc')

        violation = Violation(
            violationName=violationName,
            violationDesc=violationDesc,
            violationOwner= car.id,
            violationAddedBy=current_user.id
        )
        db.session.add(violation)
        db.session.commit()

        return redirect('/car')

    return render_template('/violationCRUD/addViolation.html',car=car)

@violationBlueprint.route('view', methods=['GET', 'POST'])
@login_required
def viewViolation():
    id = request.args.get('id')
    violation = Violation.query.filter_by(id=id).first()
    violationAddedByName = Admin.query.filter_by(id=violation.violationAddedBy).first()
    violationAddedByName = violationAddedByName.name

    car = Car.query.filter_by(id=violation.violationOwner).first()
    return render_template("/violationCRUD/viewViolation.html",violation=violation,violationAddedByName=violationAddedByName,car=car)


@violationBlueprint.route('update', methods=['GET', 'POST'])
@login_required
def updateViolation():
    id = request.args.get('id')
    violation = Violation.query.filter_by(id=id).first()
    car = Car.query.filter_by(id=violation.violationOwner).first()
    violationAddedByName = Admin.query.filter_by(id=violation.violationAddedBy).first()
    violationAddedByName = violationAddedByName.name

    if request.method == "POST":
        violationName = request.form.get('violationName')
        violationDesc = request.form.get('violationDesc')
        isResolved = request.form.get('isResolved')
        print(isResolved)
        if isResolved:
            isResolved = True
            violation.isResolved = isResolved
            if not violation.resolvedDate:
                violation.resolvedDate = now
        else:
            violation.isResolved = isResolved
            violation.resolvedDate = None

        
        violation.violationName = violationName
        violation.violationDesc = violationDesc

        db.session.commit()
        return redirect(f'/violation/view?id={id}')













    return render_template("/violationCRUD/updateViolation.html",violation=violation,car=car,violationAddedByName=violationAddedByName)
