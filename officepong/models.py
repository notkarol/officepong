from officepong import db
from datetime import datetime
from time import time

class Player(db.Model):
    name = db.Column(db.String(16), primary_key=True)
    elo = db.Column(db.Float, default=1500)

    def __init__(self, name=None, elo=None):
        super(Player, self)
        self.name = name
        self.elo = elo
        
    def __repr__(self):
        return "%s-%i" % (self.name, self.elo)


class Match(db.Model):
    timestamp = db.Column(db.Float, primary_key=True)
    winners = db.Column(db.String(32))
    losers = db.Column(db.String(32))
    winning_score = db.Column(db.Integer())
    losing_score = db.Column(db.Integer())
    
    def __init__(self, winners=None, losers=None, winning_score=None, losing_score=None):
        super(Match, self)
        self.timestamp = time()
        self.winners = winners
        self.losers = losers
        self.winning_score = None if winning_score is None else winning_score
        self.losing_score = None if losing_score is None else losing_score

    def __repr__(self):
        date_str = datetime.fromtimestamp(int(self.timestamp)).strftime("%Y-%m-%d %H:%M:%S")
        return "%s %s:%s (%i:%i)" % (date_str, self.winners, self.losers,
                                     self.winning_score, self.losing_score)
