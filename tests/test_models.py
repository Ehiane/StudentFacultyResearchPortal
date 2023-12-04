import warnings
warnings.filterwarnings("ignore")
import os
basedir = os.path.abspath(os.path.dirname(__file__))
 
from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.Model.models import User, Student, Faculty, Position, Field, Application
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

    def test_post_1(self):
        # u1 = User(username='john', email='john.yates@wsu.com')
        # db.session.add(u1)
        # db.session.commit()
        # self.assertEqual(u1.get_user_posts().all(), [])
        # p1 = Post(title='My post', body='This is my test post.', happiness_level=1, user_id=u1.id)
        # db.session.add(p1)
        # db.session.commit()
        # self.assertEqual(u1.get_user_posts().count(), 1)
        # self.assertEqual(u1.get_user_posts().first().title, 'My post')
        # self.assertEqual(u1.get_user_posts().first().body, 'This is my test post.')
        # self.assertEqual(u1.get_user_posts().first().happiness_level, 1)
        pass

    def test_student(self):
        # creating a user:
        u1 = User(username='jhon', email='jhon.yates@wsu.edu')
        db.session.add(u1)
        db.session.commit()

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



    def test_post_2(self):
        # u1 = User(username='john', email='john.yates@wsu.com')
        # u2 = User(username='amit', email='amit.khan@wsu.com')
        # db.session.add(u1)
        # db.session.add(u2)
        # db.session.commit()
        # self.assertEqual(u1.get_user_posts().all(), [])
        # self.assertEqual(u2.get_user_posts().all(), [])
        # p1 = Post(title='My post 1', body='This is my first test post.', happiness_level=1, user_id=u1.id)
        # db.session.add(p1)
        # p2 = Post(title='My post 2', body='This is my second test post.', happiness_level=3, user_id=u1.id)
        # db.session.add(p2)
        # db.session.commit()
        # p3 = Post(title='Another post', body='This is a post by somebody else.', happiness_level=2, user_id=u2.id)
        # db.session.add(p3)
        # db.session.commit()
        # # test the posts by the first user
        # self.assertEqual(u1.get_user_posts().count(), 2)
        # self.assertEqual(u1.get_user_posts().all()[1].title, 'My post 2')
        # self.assertEqual(u1.get_user_posts().all()[1].body, 'This is my second test post.')
        # self.assertEqual(u1.get_user_posts().all()[1].happiness_level, 3)
        # # test the posts by the second user
        # self.assertEqual(u2.get_user_posts().count(), 1)
        # self.assertEqual(u2.get_user_posts().all()[0].title, 'Another post')
        # self.assertEqual(u2.get_user_posts().all()[0].body, 'This is a post by somebody else.')
        # self.assertEqual(u2.get_user_posts().all()[0].happiness_level, 2)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)