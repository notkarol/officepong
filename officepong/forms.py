from flask_wtf import FlaskForm
from wtforms import StringField, IntegerRangeField, validators

class RegisterForm(FlaskForm):
    name = StringField('name', [validators.Length(min=1, max=16)])

class ScoreForm(FlaskForm):
    winners = StringField('winners', [validators.Length(min=1, max=32)])
    losers = StringField('losers', [validators.Length(min=1, max=32)])
    winning_score = IntegerField('winning_score', [validators.NumberRange(min=1, max=100)])
    losing_score = IntegerField('losing_score', [validators.NumberRange(min=0, max=100)])
