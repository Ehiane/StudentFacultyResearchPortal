from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length, Email
from app.Model.models import User, Experience, Field
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput

class FacultyRegistrationForm(FlaskForm):
    firstName = StringField('First Name',validators=[DataRequired()])
    lastName = StringField('Last Name',validators=[DataRequired()])
    wsuID = IntegerField('WSU ID',validators=[DataRequired()])
    username = StringField('Username',validators=[DataRequired()])
    phone = IntegerField('Phone Number',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    department = StringField('Department', validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    password2 = PasswordField('Repeat Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_username(self,username):
        user1 = User.query.filter_by(username=username.data).first()
        if user1 is not None:
            raise ValidationError('The username already exists! Please use a different username.')

    def validate_email(self,email):
        user1 = User.query.filter_by(email=email.data).first()
        if user1 is not None:
            raise ValidationError('The email already exists! Please use a different email address.')
        
class StudentRegistrationForm(FlaskForm):
    firstName = StringField('First Name',validators=[DataRequired()])
    lastName = StringField('Last Name',validators=[DataRequired()])
    wsuID = IntegerField('WSU ID',validators=[DataRequired()])
    username = StringField('Username',validators=[DataRequired()])
    phone = IntegerField('Phone Number',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    field = QuerySelectMultipleField('Interested Research Fields', query_factory= lambda : Field.query.all(), get_label = lambda x : Field.query.filter_by(name=x.name).first(), widget=ListWidget(prefix_label=False), option_widget=CheckboxInput())
    experience = QuerySelectMultipleField('Previous Experience:', query_factory= lambda : Experience.query.all(), get_label = lambda x : Experience.query.filter_by(name=x.name).first(), widget=ListWidget(prefix_label=False), option_widget=CheckboxInput())
    gpa = StringField('GPA',validators=[DataRequired()])
    grad_date = StringField('Graduation Date',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    password2 = PasswordField('Repeat Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_username(self,username):
        user1 = User.query.filter_by(username=username.data).first()
        if user1 is not None:
            raise ValidationError('The username already exists! Please use a different username.')

    def validate_email(self,email):
        user1 = User.query.filter_by(email=email.data).first()
        if user1 is not None:
            raise ValidationError('The email already exists! Please use a different email address.')
        

# ----------------------------------------Ehiane-Login-Attempt------------------------------------------- #
class LoginForm(FlaskForm): 
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField("Sign In")