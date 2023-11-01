from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from config import Config

from app import db
from app.Model.models import User, Faculty
from app.Controller.auth_forms import FacultyRegistrationForm

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