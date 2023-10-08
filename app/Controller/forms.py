from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.validators import  DataRequired, Length
from wtforms.widgets import ListWidget, CheckboxInput

from app.Model.models import Position, Experience, Field

class PositionForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    startDate = StringField('Start Date', validators=[DataRequired()])
    endDate = StringField('End Date', validators=[DataRequired()])
    timeCommitment = IntegerField('Time Commitment', validators=[DataRequired()])
    field = QuerySelectMultipleField('Research Fields', query_factory= lambda : Field.query.all(), get_label = lambda x : Field.query.filter_by(name=x.name).first(), widget=ListWidget(prefix_label=False), option_widget=CheckboxInput())
    experience = QuerySelectMultipleField('Experience', query_factory= lambda : Experience.query.all(), get_label = lambda x : Experience.query.filter_by(name=x.name).first(), widget=ListWidget(prefix_label=False), option_widget=CheckboxInput())
    qualifications = StringField('Qualifications', validators=[DataRequired()])
    facultyName = StringField('Faculty Name', validators=[DataRequired()])
    facultyContact = StringField('Faculty Contact', validators=[DataRequired()])
    submit = SubmitField('Submit')
