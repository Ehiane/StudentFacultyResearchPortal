from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from config import Config

from app import db
from app.Model.models import Position, Experience, Field
from app.Controller.forms import PositionForm

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'


@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/index', methods=['GET'])
def index():
    positions = Position.query.order_by(Position.title.desc())
    return render_template('index.html', title="Project Portal", positions=positions.all())

@bp_routes.route('/postposition', methods=['GET','POST'])
def postposition():
    pform = PositionForm()
    if pform.validate_on_submit():
        newPosition = Position(title = pform.title.data, description = pform.description.data, startDate = pform.startDate.data, endDate = pform.endDate.data, timeCommitment = pform.timeCommitment.data, qualifications = pform.qualifications.data, facultyName = pform.facultyName.data, facultyContact = pform.facultyContact.data)
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
