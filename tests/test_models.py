import warnings
warnings.filterwarnings("ignore")
import os
basedir = os.path.abspath(os.path.dirname(__file__))

from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.Model.models import User, Student, Faculty, Position, Field, Application, Experience
from config import Config

# NOTE - how to run a function in the terminal: 
# 'python -m unittest tests.test_models.TestModels.<name_of_function>'

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ROOT_PATH = '..//'+basedir
    
class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username='john', email='john.yates@wsu.edu')
        u.set_password('covid')
        self.assertFalse(u.get_password('flu'))
        self.assertTrue(u.get_password('covid'))


    def test_student(self):
        # observing the student db
        initial_student_count = Student.query.count()
        
        # creating a student
        s1 = Student(gpa='4.0', grad_date='2023-05-01')
        db.session.add(s1)
        db.session.commit()

        # observing the student db
        updated_student_count = Student.query.count()
        
        # checking if the object in the database is a Student
        self.assertEqual(s1.user_type,'Student')

        # checking the grad_dates match
        suspected_grad_date = Student.query.filter_by(id=s1.id).first().grad_date
        self.assertEqual(suspected_grad_date, '2023-05-01')

        # checking if the database has increased by 1
        self.assertEqual(updated_student_count,initial_student_count+1) 

    
    def test_student_relationships(self):
        # Create a Student
        s1 = Student(username='john', email='john.yates@wsu.com',gpa='4.0', grad_date='2023-05-01')
        db.session.add(s1)
        db.session.commit()

        # Add some fields and experiences to the student
        field1 = Field(name='Computer Science')
        experience1 = Experience(name='Internship')

        s1.fields.append(field1)
        s1.experiences.append(experience1)
        db.session.commit()

        # Test relationships with fields and experiences
        self.assertIn(field1, s1.fields.all())
        self.assertIn(experience1, s1.experiences.all())

    
    def test_faculty_relationships(self):
        # Create a Faculty
        f1 = Faculty(username='prof_smith', email='prof.smith@wsu.edu', department='Computer Science')
        db.session.add(f1)
        db.session.commit()

        # Add some positions to the faculty
        position1 = Position(title='Professor')
        position2 = Position(title='Associate Professor')

        f1.positions.append(position1)
        f1.positions.append(position2)
        db.session.commit()

        # Test relationships with positions
        self.assertIn(position1, f1.positions.all())
        self.assertIn(position2, f1.positions.all())
        






if __name__ == '__main__':
    unittest.main(verbosity=2)