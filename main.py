import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return flask.render_template('home.html')


app.run()
