"""
Initialize the Flask app.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://%s/officepong.db' % os.environ['HOME']

db = SQLAlchemy(app)

from officepong import routes, models
