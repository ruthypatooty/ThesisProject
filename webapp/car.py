from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Car, Violation
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime


carBlueprint = Blueprint('car', __name__)

@carBlueprint.route('/')
@login_required
def car():
    cars = Car.query.all()

    return render_template("carHome.html",cars=cars)


@carBlueprint.route('add', methods=['GET', 'POST'])
@login_required
def addCar():
    if request.method == "POST":
        print(request.form)
        plateNumber = request.form.get('plateNumber')
        engineNumber = request.form.get('engineNumber')
        if engineNumber == "":
            engineNumber = None
        ownerName = request.form.get('ownerName')
        ownerContact = request.form.get('ownerContact')
        isHotplate = request.form.get('isHotplate')
        if isHotplate:
            isHotplate = True
        else:
            isHotplate = False
        print(isHotplate)
        new_car = Car(plateNumber=plateNumber, engineNumber=engineNumber,ownerName=ownerName,ownerContact=ownerContact,isHotplate=isHotplate)

        db.session.add(new_car)
        db.session.commit()

        return redirect(url_for('car.car'))




    
    return render_template("/carCRUD/addCar.html")


@carBlueprint.route('view', methods=['GET', 'POST'])
@login_required
def viewCar():
    id = request.args.get('id')
    car = Car.query.filter_by(id=id).first()
    violations = Violation.query.filter_by(violationOwner=car.id)
    return render_template("/carCRUD/viewCar.html",car=car,violations=violations )



@carBlueprint.route('delete', methods=['GET', 'POST'])
@login_required
def deleteCar():
    id = request.args.get('id')
    car = Car.query.filter_by(id=id).first()
    db.session.delete(car)
    db.session.commit()
    return redirect('/car')


@carBlueprint.route('update', methods=['GET', 'POST'])
@login_required
def updateCar():
    
    id = request.args.get('id')
    car = Car.query.filter_by(id=id).first()
    if request.method == "POST":
        engineNumber = request.form.get('engineNumber')
        if engineNumber == "":
            engineNumber = None
        ownerName = request.form.get('ownerName')
        ownerContact = request.form.get('ownerContact')
        isHotplate = request.form.get('isHotplate')
        if isHotplate:
            isHotplate = True
        else:
            isHotplate = False
        lastSeenLoc = request.form.get('lastSeenLoc')
        lastSeenDate = request.form.get('lastSeenDate')
    
        if lastSeenDate:
            lastSeenDate = datetime.strptime(lastSeenDate,"%Y-%m-%dT%H:%M")
            car.lastSeenDate = lastSeenDate

   

        car.engineNumber = engineNumber
        car.ownerName = ownerName
        car.ownerContact = ownerContact
        car.isHotplate = isHotplate
        car.lastSeenLoc = lastSeenLoc
        
        db.session.commit()
        return redirect(f'/car/view?id={id}')


    return render_template("/carCRUD/viewCar.html",car=car )

@carBlueprint.route('/', methods=['POST'])
@login_required
def filerCarbyLicense():
    if request.method == 'POST':
        print(request.form.get('plateNumber'))
        searchKey = request.form.get('plateNumber')
        search = "%{}%".format(searchKey)
        cars = Car.query.filter(Car.plateNumber.like(search)).all()
        print(cars)
        return render_template("carHome.html",cars=cars)

    return redirect('/car')