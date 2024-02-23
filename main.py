import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager


app = Flask(__name__)
app.app_context().push()  # https://stackoverflow.com/questions/31444036/runtimeerror-working-outside-of-application-context
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
db.create_all()


@app.route('/')
def home():
    return flask.render_template('home.html')


@app.route('/about')
def about():
    return flask.render_template('about.html')


@app.route('/questions')
def questions():
    return flask.render_template('questions.html')

@app.route('/login')
def login():
    return flask.render_template('login.html')

@app.route('/register')
def register():
    return flask.render_template('register.html')