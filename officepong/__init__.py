from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from officepong.config import Config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/officepong.db'
app.config['SECRET_KEY'] = 'Table Tennis'
app.config['WTF_CSRF_SECRET_KEY'] = 'Ping Pong'
db = SQLAlchemy(app)
from officepong import routes, models
