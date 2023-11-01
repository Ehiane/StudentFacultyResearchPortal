from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Login loader
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# Table of Many-to-Many relationship for Position and Experiences model
positionExperiences = db.Table('positionExperiences',
    db.Column('position_id', db.Integer, db.ForeignKey('position.id')),
    db.Column('experience_id', db.Integer, db.ForeignKey('experience.id'))
)

# Table of Many-to-Many relationship for Position and Research Fields model
positionFields = db.Table('positionFields',
    db.Column('position_id', db.Integer, db.ForeignKey('position.id')),
    db.Column('field_id', db.Integer, db.ForeignKey('field.id'))
)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'))
    # student_id (milestone3)
    # need to implement relationship between student and application (milestone 3)
    statement = db.Column(db.String(1500))
    referenceName = db.Column(db.String(20))
    referenceEmail = db.Column(db.String(50))

class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(1000))
    startDate = db.Column(db.String(30))
    endDate = db.Column(db.String(30))
    timeCommitment = db.Column(db.Integer())
    # By defining the research fields and experiences as models in the database,
    # users are able to add additional fields and experiences later if there isn't one already present they need.
    fields = db.relationship('models.Field',secondary=positionFields, primaryjoin=(positionFields.c.position_id == id), backref=db.backref('positionFields', lazy='dynamic'), lazy='dynamic')
    experiences = db.relationship('models.Experience',secondary=positionExperiences, primaryjoin=(positionExperiences.c.position_id == id), backref=db.backref('positionExperiences', lazy='dynamic'), lazy='dynamic')
    qualifications = db.Column(db.String(300))
    facultyName = db.Column(db.String(30))
    facultyContact = db.Column(db.String(50))
    # One to many relationship between position and applications
    applications = db.relationship('Application', backref='position', lazy='dynamic')

    def get_experiences(self):
        return self.experiences
    def get_fields(self):
        return self.fields
    def get_applications(self):
        return self.applications
    
class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    positions = db.relationship('models.Position', secondary=positionExperiences, primaryjoin=(positionExperiences.c.experience_id == id), backref=db.backref('positionExperiences', lazy='dynamic'), lazy='dynamic')
    def __repr__(self):
       return '{}'.format(self.name)
   
class Field(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    positions = db.relationship('models.Position', secondary=positionFields, primaryjoin=(positionFields.c.field_id == id), backref=db.backref('positionField', lazy='dynamic'), lazy='dynamic')
    def __repr__(self):
       return '{}'.format(self.name)
   
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    # Hidden ID
    id = db.Column(db.Integer, primary_key=True)
    # Account Info
    username = db.Column(db.String(64), unique=True, index =True)
    password_hash = db.Column(db.String(128))
    # Contact Info
    firstName = db.Column(db.String(64))
    lastName = db.Column(db.String(64))
    wsuID = db.Column(db.Integer)
    email = db.Column(db.String(128))
    phone = db.Column(db.String(20))
    user_type = db.Column(db.String(50))
    
    # Relationship
    __mapper_args__ = {
        'polymorphic_identity': 'User',
        'polymorphic_on': user_type
        
    }
    
    def __repr__(self):
        return '<User: {} - {};>'.format(self.username,self.wsuID)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def get_password(self, password):
        return check_password_hash(self.password_hash, password)
    def get_user_posts(self):
        return self.posts
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

class Faculty(User):
    __tablename__ = 'faculty'
    # Hidden ID
    id = db.Column(db.ForeignKey("user.id"), primary_key=True)
    # Faculty Info
    department = db.Column(db.String(64))
    # Relationship
    __mapper_args__ = {
        'polymorphic_identity': 'Faculty'
    }
    
class Student(User):
    __tablename__ = 'student'
    # Hidden ID
    id = db.Column(db.ForeignKey("user.id"), primary_key=True)
    # Faculty Info
    department = db.Column(db.String(64))
    gpa = db.Column(db.String(10))
    grad_date = db.Column(db.String(30))
    # Relationship
    __mapper_args__ = {
        'polymorphic_identity': 'Student'
    }