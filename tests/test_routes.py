"""
This file contains the functional tests for the routes.
These tests use GETs and POSTs to different URLs to check for the proper behavior.
Resources:
    https://flask.palletsprojects.com/en/1.1.x/testing/ 
    https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/ 
"""
import os
import pytest
from app import create_app, db
from app.Model.models import (
    User,
    Student,
    Faculty,
    Position,
    Field,
    Application,
    Experience,
)
from config import Config


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
    SECRET_KEY = "bad-bad-key"
    WTF_CSRF_ENABLED = False
    DEBUG = True
    TESTING = True


@pytest.fixture(scope="module")
def test_client():
    # create the flask application ; configure the app for tests
    flask_app = create_app(config_class=TestConfig)

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client
    # this is where the testing happens!

    ctx.pop()


def new_user(uname, uemail, passwd):
    user = User(username=uname, email=uemail)
    user.set_password(passwd)
    return user


@pytest.fixture
def init_database():
    # Create the database and the database table
    db.create_all()
    # initialize the tags
    # init_tags()
    #add faculty and student 
    f1 = Faculty(username='professor', email='professor@wsu.edu', department='Computer Science')
    s1 = Student(username='student', email='student@wsu.edu', gpa='3.0', grad_date='2023-05-01')
    # Insert user data
    db.session.add(f1)
    db.session.add(s1)
    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()

#giving sql lite internal error:   sqlite3.OperationalError: no such table: field
# def test_student_register_page(test_client):
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/studentregister' page is requested (GET)
#     THEN check that the response is valid
#     """
#     # Create a test client using the Flask application configured for testing
#     response = test_client.get("/studentregister")
#     assert response.status_code == 200
#     assert b"Register" in response.data


def test_faculty_register_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/facultyregister' page is requested (GET)
    THEN check that the response is valid
    """
    # Create a test client using the Flask application configured for testing
    response = test_client.get("/facultyregister")
    assert response.status_code == 200
    assert b"Register" in response.data


def test_student_register(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' form is submitted (POST)
    THEN check that the response is valid and the database is updated correctly
    """
    # Create a test client using the Flask application configured for testing
    response = test_client.post(
        "/studentregister",
        data=dict(
            firstName="john",
            lastName="doe",
            wsuID=11241901,
            phone=4258660288,
            field=["Software Engineering", "Computer Science"],
            experience=["C", "C++"],
            gpa="3.6",
            grad_date="06-05-2025",
            username="john",
            email="john@wsu.edu",
            password="bad-bad-password",
            password2="bad-bad-password",
        ),
        follow_redirects=True,
    )
    assert response.status_code == 200


    s = db.session.query(User).filter(User.username == "john")
    print(s.first())  # Add this line to inspect the user in the console


    assert s.first().email == "john@wsu.edu"
    assert s.count() == 1
    # verifiying that you have been redirected to the index page
    assert response.request.path == "/index"
    assert b"Please register or sign in to view/create open positions." in response.data
  

def test_invalidlogin(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' form is submitted (POST) with wrong credentials
    THEN check that the response is valid and login is refused
    """
    response = test_client.post(
        "/login",
        data=dict(username="sakire", password="12345", remember_me=False),
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert (
        b"Invalid username or password" in response.data
    )  # You may update the assertion condition according to the content of your login page.


def test_login_logout(request, test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' form is submitted (POST) with correct credentials
    THEN check that the response is valid and login is succesfull
    """
    response = test_client.post(
        "/login",
        data=dict(username="sakire", password="1234", remember_me=False),
        follow_redirects=True,
    )
    assert response.status_code == 200
    
    response = test_client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"Sign In" in response.data
    assert response.request.path == "/login"
  
def test_postPosition(test_client, init_database):
    # Create sample Field and Experience instances
    field_instance1 = Field(name="Software Engineering")
    field_instance2 = Field(name="Computer Science")

    experience_instance1 = Experience(name="C")
    experience_instance2 = Experience(name="C++")

    # Add instances to the database
    db.session.add_all([field_instance1, field_instance2, experience_instance1, experience_instance2])
    db.session.commit()

    # Login as a faculty user
    faculty_user = Faculty(
        username="w.rae",
        email="w.rae@wsu.edu",
        department="Computer Science",
    )
    faculty_user.set_password("1234")
    db.session.add(faculty_user)
    db.session.commit()

    response = test_client.post(
        '/login',
        data=dict(username='w.rae', password='1234', remember_false=False),
        follow_redirects=True
    )

    assert response.status_code == 200

    # Access postposition page
    response = test_client.get("/postposition")
    assert response.status_code == 200
    assert b"Create New Position" in response.data

    # Post position with the created Field and Experience instances
    response = test_client.post('/postposition',
                                data=dict(title='test_post',
                                          description='This is a test post',
                                          startDate='06/05/2023',
                                          endDate='12/06/2025',
                                          timeCommitment=3,
                                          fields=[field_instance1, field_instance2],
                                          experiences=[experience_instance1, experience_instance2],
                                          qualifications='Experience',
                                          facultyName='EECS Computer',
                                          facultyContact='Sakire Arslan-Ay'
                                          ),
                                follow_redirects=True
                                )



    assert response.status_code == 200
    assert b"test_post" in response.data
    assert b"This is a test post" in response.data

    # Query the database to check if the position is created
    positions = db.session.query(Position).filter(Position.title == "test_post").all()

    # Check the positions in the database
    print("Positions in the database:", positions)

    # Assert that at least one position is created
    assert len(positions) == 1



# def test_postSmile(test_client, init_database):
#     """
#     GIVEN a Flask application configured for testing , after user logs in,
#     WHEN the '/postsmile' page is requested (GET)  AND /PostForm' form is submitted (POST)
#     THEN check that response is valid and the class is successfully created in the database
#     """
#     # login
#     response = test_client.post(
#         "/login",
#         data=dict(username="sakire", password="1234", remember_me=False),
#         follow_redirects=True,
#     )
#     assert response.status_code == 200
#     assert (
#         b"Welcome to Smile Portal!" in response.data
#     )  # You may update the assertion condition according to the content of your  page.

#     # test the "PostSmile" form
#     response = test_client.get("/postsmile")
#     assert response.status_code == 200
#     assert (
#         b"Post New Smile" in response.data
#     )  # You may update the assertion condition according to the content of your  page.

#     # test posting a smile story
#     tags1 = list(
#         map(lambda t: t.id, Tag.query.all()[:3])
#     )  # should only pass 'id's of the tags. See https://stackoverflow.com/questions/62157168/how-to-send-queryselectfield-form-data-to-a-flask-view-in-a-unittest
#     print("TESTING********************: ", tags1)
#     response = test_client.post(
#         "/postsmile",
#         data=dict(
#             title="My test post",
#             body="This is my first test post.",
#             happiness_level=2,
#             tag=tags1,
#         ),
#         follow_redirects=True,
#     )
#     assert response.status_code == 200
#     assert (
#         b"Welcome to Smile Portal!" in response.data
#     )  # You may update the assertion condition according to the content of your  page.
#     assert b"My test post" in response.data
#     assert b"This is my first test post." in response.data

#     c = db.session.query(Post).filter(Post.title == "My test post")
#     assert c.first().get_tags().count() == 3  # should have 3 tags
#     assert (
#         c.count() >= 1
#     )  # There should be at least one post with body "Here is another post."

#     tags2 = list(
#         map(lambda t: t.id, Tag.query.all()[1:3])
#     )  # should only pass 'id's of the tags. See https://stackoverflow.com/questions/62157168/how-to-send-queryselectfield-form-data-to-a-flask-view-in-a-unittest
#     print("TESTING********************: ", tags2)
#     response = test_client.post(
#         "/postsmile",
#         data=dict(
#             title="Second post",
#             body="Here is another post.",
#             happiness_level=1,
#             tag=tags2,
#         ),
#         follow_redirects=True,
#     )
#     assert response.status_code == 200
#     assert (
#         b"Welcome to Smile Portal!" in response.data
#     )  # You may update the assertion condition according to the content of your  page.
#     assert b"Second post" in response.data
#     assert b"Here is another post." in response.data

#     c = db.session.query(Post).filter(Post.body == "Here is another post.")
#     assert c.first().get_tags().count() == 2  # Should have 2 tags
#     assert (
#         c.count() >= 1
#     )  # There should be at least one post with body "Here is another post."

#     assert db.session.query(Post).count() == 2

#     # finally logout
#     response = test_client.get("/logout", follow_redirects=True)
#     assert response.status_code == 200
#     assert b"Sign In" in response.data
#     assert (
#         b"Please log in to access this page." in response.data
#     )  # You may update the assertion condition according to the content of your  page.


# def test_likeSmile(test_client, init_database):
#     """
#     GIVEN a Flask application configured for testing , after user logs-in,
#      /like form is submitted (POST)
#     THEN check that response is valid and the like count is updated in the database
#     """
#     # login
#     response = test_client.post(
#         "/login",
#         data=dict(username="sakire", password="1234", remember_me=False),
#         follow_redirects=True,
#     )
#     assert response.status_code == 200
#     assert (
#         b"Welcome to Smile Portal!" in response.data
#     )  # You may update the assertion condition according to the content of your  page.

#     # first post two smile stories
#     response = test_client.get("/postsmile")
#     assert response.status_code == 200
#     tags1 = list(
#         map(lambda t: t.id, Tag.query.all()[:3])
#     )  # should only pass 'id's of the tags. See https://stackoverflow.com/questions/62157168/how-to-send-queryselectfield-form-data-to-a-flask-view-in-a-unittest
#     response = test_client.post(
#         "/postsmile",
#         data=dict(
#             title="My test post",
#             body="This is my first test post.",
#             happiness_level=2,
#             tag=tags1,
#         ),
#         follow_redirects=True,
#     )
#     assert response.status_code == 200
#     c1 = db.session.query(Post).filter(Post.title == "My test post")
#     assert (
#         c1.count() >= 1
#     )  # There should be at least one post with body "Here is another post."

#     tags2 = list(
#         map(lambda t: t.id, Tag.query.all()[1:3])
#     )  # should only pass 'id's of the tags. See https://stackoverflow.com/questions/62157168/how-to-send-queryselectfield-form-data-to-a-flask-view-in-a-unittest
#     response = test_client.post(
#         "/postsmile",
#         data=dict(
#             title="Second post",
#             body="Here is another post.",
#             happiness_level=1,
#             tag=tags2,
#         ),
#         follow_redirects=True,
#     )
#     assert response.status_code == 200
#     c2 = db.session.query(Post).filter(Post.body == "Here is another post.")
#     assert (
#         c2.count() >= 1
#     )  # There should be at least one post with body "Here is another post."
#     assert c2.first().likes == 0
#     assert db.session.query(Post).count() == 2

#     # like the second post
#     response = test_client.post(
#         "/like/" + str(c2.first().id), data={}, follow_redirects=True
#     )
#     assert response.status_code == 200
#     # The page should be redirected to the main page
#     assert (
#         b"Welcome to Smile Portal!" in response.data
#     )  # You may update the assertion condition according to the content of your  page.
#     # check whether the likecount was updated successfully
#     c3 = db.session.query(Post).filter(Post.id == c1.first().id)
#     assert c3.first().likes == 0
#     c4 = db.session.query(Post).filter(Post.id == c2.first().id)
#     assert c4.first().likes == 1


if __name__ == "__main__":
    t_db = init_database()
    print(t_db)

