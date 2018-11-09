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
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(16), unique=True)
    elo = db.Column(db.Float(), default=1500)
    games = db.Column(db.Integer(), default=0)
    win_rate = db.Column(db.Float(), default=0)

    def __init__(self, name):
        super(Player, self)
        self.id = None
        self.name = name
        self.elo = None
        self.games = None
        self.win_rate = None

    def __repr__(self):
        return "%s-%i-%i-%i" % (self.name, self.elo, self.games, self.win_rate)

class Team(db.Model):
    """
    A team is two players.
    """
    id = db.Column(db.Integer(), primary_key=True)
    player1_id = db.Column(db.Integer())
    player2_id = db.Column(db.Integer())
    elo = db.Column(db.Float(), default=1500)
    games = db.Column(db.Integer(), default=0)
    win_rate = db.Column(db.Float(), default=0)

    def __init__(self, player1_id=None, player2_id=None):
        super(Team, self)
        self.id = None
        self.player1_id = player1_id
        self.player2_id = player2_id
        self.elo = None
        self.games = None
        self.win_rate = None

    def __repr__(self):
        return "%i-%i-%i-%i-%i" % (self.player1_id, self.player2_id, self.elo, self.games, self.win_rate)


class SinglesMatch(db.Model):
    """
    A match is a game, it can have multiple winners and losers, and a
    a score for the winners and losers.
    """
    timestamp = db.Column(db.Integer(), primary_key=True)
    win_user_id = db.Column(db.Integer())
    lose_user_id = db.Column(db.Integer())
    win_score = db.Column(db.Integer())
    lose_score = db.Column(db.Integer())
    expected = db.Column(db.Float())
    elo_delta = db.Column(db.Float())

    def __init__(self, win_user_id=None, lose_user_id=None, win_score=None, 
                 lose_score=None, expected=None, elo_delta=None):
        super(SinglesMatch, self)
        self.timestamp = int(time())
        self.win_user_id = win_user_id
        self.lose_user_id = lose_user_id
        self.win_score = win_score
        self.lose_score = lose_score
        self.expected = expected
        self.elo_delta = elo_delta

    def __repr__(self):
        return "%i %s:%s (%i:%i) %i" % (self.timestamp, self.win_user_id, self.lose_user_id,
                                        self.win_score, self.lose_score, self.elo_delta)



class DoublesMatch(db.Model):
    """
    A match is a game, it can have multiple winners and losers, and a
    a score for the winners and losers.
    """
    timestamp = db.Column(db.Integer(), primary_key=True)
    win_team_id = db.Column(db.Integer())
    lose_team_id = db.Column(db.Integer())
    win_score = db.Column(db.Integer())
    lose_score = db.Column(db.Integer())
    expected = db.Column(db.Float())
    elo_delta = db.Column(db.Float())

    def __init__(self, win_team_id=None, lose_team_id=None, win_score=None, 
                 lose_score=None, expected=None, elo_delta=None):
        super(SinglesMatch, self)
        self.timestamp = int(time())
        self.win_team_id = win_team_id
        self.lose_team_id = lose_team_id
        self.win_score = win_score
        self.lose_score = lose_score
        self.expected = expected
        self.elo_delta = elo_delta

    def __repr__(self):
        return "%i %s:%s (%i:%i) %i" % (self.timestamp, self.win_team_id, self.lose_team_id,
                                        self.win_score, self.lose_score, self.elo_delta)
