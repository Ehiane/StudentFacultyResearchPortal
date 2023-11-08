from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from config import Config
from flask_login import login_user, current_user, logout_user, login_required

from app import db
from app.Model.models import User, Faculty, Student, Field, Experience
from app.Controller.auth_forms import FacultyRegistrationForm, StudentRegistrationForm

bp_auth = Blueprint('auth', __name__)
bp_auth.template_folder = Config.TEMPLATE_FOLDER 

@bp_auth.route('/facultyregister', methods=['GET', 'POST'])
def facultyRegister():
    frform = FacultyRegistrationForm()
    if frform.validate_on_submit():
        # Set Faculty Data
        newFaculty = Faculty(department=frform.department.data)
        # Set User Data
        newFaculty.username = frform.username.data
        newFaculty.firstname = frform.firstName.data
        newFaculty.lastName = frform.lastName.data
        newFaculty.wsuID = frform.wsuID.data
        newFaculty.email = frform.email.data
        newFaculty.phone = frform.phone.data
        newFaculty.user_type = "Faculty"
        # Set Password
        newFaculty.set_password(frform.password.data)
        db.session.add(newFaculty)
        db.session.commit()
        flash('Congratulations, you are now registered as a faculty user!')
        return redirect(url_for('routes.index'))
    return render_template('facultyRegister.html', form = frform)

@bp_auth.route('/studentregister', methods=['GET', 'POST'])
def studentRegister():
    srform = StudentRegistrationForm()
    if srform.validate_on_submit():
        # Set Faculty Data
        newStudent = Student(gpa=srform.gpa.data, grad_date=srform.grad_date.data)
        # Set User Data
        newStudent.username = srform.username.data
        newStudent.firstname = srform.firstName.data
        newStudent.lastName = srform.lastName.data
        newStudent.wsuID = srform.wsuID.data
        newStudent.email = srform.email.data
        newStudent.phone = srform.phone.data
        newStudent.user_type = "Student"
        # Set Password
        newStudent.set_password(srform.password.data)
        # Set Relation Stuff
        for x in srform.experience.data:
            e = Experience.query.filter_by(name=x.name).first()
            newStudent.experiences.append(e)
        for y in srform.field.data:
            f = Field.query.filter_by(name=y.name).first()
            newStudent.fields.append(f)
        db.session.add(newStudent)
        db.session.commit()
        flash('Congratulations, you are now registered as a student user!')
        return redirect(url_for('routes.index'))
    return render_template('studentRegister.html', form = srform)

# ----------------------------------------Ehiane-Login-Attempt------------------------------------------- #
@bp_auth.route('/login',methods=['GET','POST'])
def login():
    #recognized user
    if current_user.is_authenticated:
        flash(" User is already logged in")
        return redirect(url_for("routes.index"))
    #unrecognized user
    lform = LoginForm()
    if lform.validate_on_submit():
        user = User.query.filter_by(username = lform.username.data).first()
        # if login fails
        if (user is None) or (user.check_password(lform.password.data) == False):
            flash("Invalid username or password")
            return redirect(url_for("auth.login"))
        # if login succeeds
        else:
            login_user(user, remember=lform.remember_me.data)
            flash(f"Login Successful for {user.username}")
            return redirect(url_for("routes.index"))
    return render_template("login.html", title = "Sign In", form=lform)

@bp_auth.route('/logout',methods=['GET','POST'])
def logout():
    logout_user()
    flash(f"Successfully logged out!")
    return redirect(url_for("auth.login"))