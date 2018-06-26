"""
Initialize the Flask app.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/officepong.db'
db = SQLAlchemy(app)

from officepong import routes, models
