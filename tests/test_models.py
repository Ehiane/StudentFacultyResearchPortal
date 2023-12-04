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
        """
        This class solely tests the Student Model.
        """
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
        """
        This class tests Fields and Experience model while using the Student class as the relationship connector
        """
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
        """
        This class tests Positions model while using the Student class as the relationship connector
        """
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

    def test_application(self):
        """
        This class mainly tests the Application Model and it's relationship with a Student
        """
        # Create a Position
        position = Position(title='Assistant Professor')
        db.session.add(position)
        db.session.commit()

        # Create a Student
        student = Student(username='jhon', email='jhon.yates@wsu.edu', gpa='4.0', grad_date='2023-05-01')
        db.session.add(student)
        db.session.commit()

        # Create an Application
        application = Application(position=position, student=student, statement='This is my application statement.', referenceName='John Doe', referenceEmail='john.doe@example.com', status=1)
        db.session.add(application)
        db.session.commit()

        # Checking if the database has increased by 1
        self.assertEqual(Application.query.count(), 1)

        # Check the properties of the application
        self.assertEqual(application.position, position)
        self.assertEqual(application.student, student)
        self.assertEqual(application.statement, 'This is my application statement.')
        self.assertEqual(application.referenceName, 'John Doe')
        self.assertEqual(application.referenceEmail, 'john.doe@example.com')
        self.assertEqual(application.status, 1)


    def test_faculty(self):
        # creating a user:
        u1 = User(username='john', email='john.yates@wsu.edu')
        db.session.add(u1)
        db.session.commit()

        # observing the faculty db
        initial_faculty_count = Faculty.query.count()
        
        # creating a student
        f1 = Faculty(department='CptS')
        db.session.add(f1)
        db.session.commit()

        # observing the faculty db
        updated_faculty_count = Faculty.query.count()

        # checking if the object in the database is Faculty
        self.assertEqual(f1.user_type,'Faculty')

        # checking the departments match
        suspected_department = Faculty.query.filter_by(id=f1.id).first().department
        self.assertEqual(suspected_department, 'CptS')

        # checking if the database has increased by 1
        self.assertEqual(updated_faculty_count,initial_faculty_count+1)





if __name__ == '__main__':
    unittest.main(verbosity=2)