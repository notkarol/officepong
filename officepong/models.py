"""
Database schema.
"""
from datetime import datetime
from time import time
from officepong import db

class Player(db.Model):
    """
    A player is a user with an ELO score.
    """
    name = db.Column(db.String(16), primary_key=True)
    elo = db.Column(db.Float, default=1500)

    def __init__(self, name=None, elo=None):
        super(Player, self)
        self.name = name
        self.elo = elo

    def __repr__(self):
        return "%s-%i" % (self.name, self.elo)


class Match(db.Model):
    """
    A match is a game, it can have multiple winners and losers, and a
    a score for the winners and losers.
    """
    timestamp = db.Column(db.Float, primary_key=True)
    winners = db.Column(db.String(32))
    losers = db.Column(db.String(32))
    winning_score = db.Column(db.Integer())
    losing_score = db.Column(db.Integer())
    expected = db.Column(db.Float())

    def __init__(self, winners=None, losers=None, winning_score=None, losing_score=None,
                 expected=None):
        super(Match, self)
        self.timestamp = time()
        self.winners = winners
        self.losers = losers
        self.winning_score = winning_score
        self.losing_score = losing_score
        self.expected = expected

    def __repr__(self):
        return "%i %s:%s (%i:%i)" % (self.timestamp, self.winners, self.losers,
                                     self.winning_score, self.losing_score)
