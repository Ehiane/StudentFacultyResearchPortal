from app import db

positionExperiences = db.Table('positionExperiences',
    db.Column('position_id', db.Integer, db.ForeignKey('position.id')),
    db.Column('experience_id', db.Integer, db.ForeignKey('experience.id'))
)

positionFields = db.Table('positionFields',
    db.Column('position_id', db.Integer, db.ForeignKey('position.id')),
    db.Column('field_id', db.Integer, db.ForeignKey('field.id'))
)

class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(1000))
    startDate = db.Column(db.String(30))
    endDate = db.Column(db.String(30))
    timeCommitment = db.Column(db.Integer())
    fields = db.relationship('models.Field',secondary=positionFields, primaryjoin=(positionFields.c.position_id == id), backref=db.backref('positionFields', lazy='dynamic'), lazy='dynamic')
    experiences = db.relationship('models.Experience',secondary=positionExperiences, primaryjoin=(positionExperiences.c.position_id == id), backref=db.backref('positionExperiences', lazy='dynamic'), lazy='dynamic')
    qualifications = db.Column(db.String(300))
    facultyName = db.Column(db.String(30))
    facultyContact = db.Column(db.String(50))
    def get_experiences(self):
        return self.experiences
    def get_fields(self):
        return self.fields
    
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