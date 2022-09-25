from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Admin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        admin = Admin.query.filter_by(email=email).first()
        if admin:
            if check_password_hash(admin.password, password):
                #flash('Logged in successfully!', category='success')
                login_user(admin, remember=True)
                return redirect('/car')
            else:
                pass
                #flash('Incorrect password, try again.', category='error')
        else:
            pass
            #flash('Email does not exist.', category='error')

    return render_template("login.html", admin=current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        print(request.form)

        #TODO 
        # 1. Data Validation

        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        adminContact = request.form.get('adminContact')

        notifyIfFoundHotPlate = False
        if request.form.get('notifyIfFoundHotPlate'):
            notifyIfFoundHotPlate = True

        new_admin = Admin(email=email, 
        password=generate_password_hash(
                password1, method='sha256'),
                notifyIfFoundHotPlate=notifyIfFoundHotPlate,
                name=name, adminContact=adminContact )
        db.session.add(new_admin)
        db.session.commit()
        login_user(new_admin, remember=True)
        #flash('Account created!', category='success')
        return redirect('/login')
        


    return render_template("sign_up.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")
