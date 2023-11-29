from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from config import Config

from app import db
from app.Model.models import Position, Experience, Field, Application
from app.Controller.forms import PositionForm, ExperienceForm, FieldForm, ApplicationForm, FilterForm
from flask_login import current_user, login_required

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'


@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/index', methods=['GET','POST'])
def index():
    positions = Position.query.all()
    #newpositions = Position.query
    fform = FilterForm()
    if fform.is_submitted(): # and current_user.user_type == 'Student':
        if fform.checkbox.data is True:
            i = 0
            for p in positions:
                num = 0
                for pfield in p.fields:
                    for ufield in current_user.fields:
                        if ufield.name == pfield.name:
                            num += 1
                if num < 1:
                    positions.pop(i)
                i += 1
            flash("Box checked")
    return render_template('index.html', title="Project Portal", positions=positions, form=fform)

@bp_routes.route('/myapplications', methods=['GET'])
@login_required
def myapplications():
    applications = Application.query.filter_by(student_id=current_user.id)
    positions = Position.query.order_by(Position.title.desc())
    return render_template('myapplications.html', applications=applications.all(), positions=positions.all())

@bp_routes.route('/mypositions', methods=['GET'])
@login_required
def mypositions():
    positions = Position.query.filter_by(faculty_id=current_user.id)
    return render_template('mypositions.html', positions=positions.all())

@bp_routes.route('/myapplicants/<position_id>', methods=['GET', 'POST'])
@login_required
def myapplicants(position_id):
    applications = Application.query.filter_by(position_id=position_id)
    position = Position.query.filter_by(id=position_id).first()
    return render_template('myapplicants.html', applications=applications.all(), position=position)

@bp_routes.route('/postposition', methods=['GET','POST'])
@login_required
def postposition():
    pform = PositionForm()
    if pform.validate_on_submit():
        newPosition = Position(title = pform.title.data, description = pform.description.data, startDate = pform.startDate.data, endDate = pform.endDate.data, timeCommitment = pform.timeCommitment.data, qualifications = pform.qualifications.data, facultyName = pform.facultyName.data, facultyContact = pform.facultyContact.data, faculty_id = current_user.id)
        for x in pform.experience.data:
            e = Experience.query.filter_by(name=x.name).first()
            newPosition.experiences.append(e)
        for y in pform.field.data:
            f = Field.query.filter_by(name=y.name).first()
            newPosition.fields.append(f)
        db.session.add(newPosition)
        db.session.commit()
        flash('New post "' + newPosition.title + '" created.')
        return redirect(url_for('routes.index'))
    return render_template('create.html', form = pform)

@bp_routes.route('/deleteposition/<position_id>', methods=['GET','POST'])
@login_required
def deleteposition(position_id):
    theposition = Position.query.filter_by(id=position_id).first()
    positionname = theposition.title
    if theposition.faculty_id == current_user.id:
        for f in theposition.fields:
            theposition.fields.remove(f)
        for e in theposition.experiences:
            theposition.experiences.remove(e)
        db.session.commit()
        db.session.delete(theposition)
        db.session.commit()
        flash('Research Position: "' + positionname + '" deleted.')
    else:
        flash('Research Position: "' + positionname + '" cannot be deleted.')
    return redirect(url_for('routes.index'))

@bp_routes.route('/deleteapplication/<application_id>', methods=['GET','POST'])
@login_required
def deleteapplication(application_id):
    theapp = Application.query.filter_by(id=application_id).first()
    if theapp.student_id == current_user.id:
        db.session.delete(theapp)
        db.session.commit()
        flash('Application deleted.')
    else:
        flash('Application cannot be deleted.')
    return redirect(url_for('routes.index'))

@bp_routes.route('/addexperience', methods=['GET','POST'])
@login_required
def addexperience():
    eform = ExperienceForm()
    if eform.validate_on_submit():
        e = eform.newExperience.data
        db.session.add(Experience(name=e))
        db.session.commit()
        flash('New experience: "' + e + '" added.')
        return redirect(url_for('routes.index'))
    return render_template('addexperience.html', form = eform)

@bp_routes.route('/addfield', methods=['GET','POST'])
@login_required
def addfield():
    fform = FieldForm()
    if fform.validate_on_submit():
        f = fform.newField.data
        db.session.add(Field(name=f))
        db.session.commit()
        flash('New research field: "' + f + '" added.')
        return redirect(url_for('routes.index'))
    return render_template('addfield.html', form = fform)

@bp_routes.route('/application/<position_id>', methods=['GET', 'POST'])
@login_required
def application(position_id):
    aform = ApplicationForm()
    thePosition = Position.query.filter_by(id=position_id).first()
    if aform.validate_on_submit():
        newApplication = Application(position_id = thePosition.id, student_id = current_user.id, statement = aform.statement.data, referenceName = aform.referenceName.data, referenceEmail = aform.referenceEmail.data)
        db.session.add(newApplication)
        db.session.commit()
        flash('You have applied for the research position!')
        return redirect(url_for('routes.index'))
    return render_template('application.html', form=aform)