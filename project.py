from app import create_app, db
from app.Model.models import Position, Experience, Field

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'Position': Position, 'Experience': Experience, 'Field': Field}

@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()
        if Experience.query.count() == 0:
            experiences = ['C','C++', 'Python', 'CSS', 'HTML', 'SQL', 'Node.js']
            fields = ['Artificial Intelligence','Software Engineering', 'Civil Engineering', 'Mechanical Engineering', 'Computer Science']
            for e in experiences:
                db.session.add(Experience(name=e))
            for f in fields:
                db.session.add(Field(name=f))
            db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
else:
    print("not main file") 
    #Ehiane: was testing out why the debug mode wasn't turned on on my end.
    #it was making the styling process harder when the debug mode was off.
