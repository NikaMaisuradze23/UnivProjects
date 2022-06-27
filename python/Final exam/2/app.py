from flask import Flask, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'python'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///person.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Oscar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column('year', db.Integer, nullable=False)
    age = db.Column('age', db.Integer,  nullable=False)
    name = db.Column('name', db.String(40), nullable=False)

    def __str__(self):
        return f'სახელი:{self.name}; წელი: {self.year}; ასაკი: {self.age}'

db.create_all()



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/person', methods=['GET', 'POST'])
def person():
    if request.method == "POST":
        y = request.form['year']
        a = request.form['age']
        n = request.form['name']
        new_user = Oscar(year=y, age=a, name=n)
        db.session.add(new_user)
        db.session.commit()
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
