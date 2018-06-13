from app import db
from datetime import datetime

class Player(db.Model):
    name = db.Column(db.String(16), primary_key=True)
    elo = db.Column(db.Float, default=1500)

    def __repr__(self):
        return "%s-%i" % (self.name, self.elo)

class Match(db.Model):
    timestamp = db.Column(db.Float, primary_key=True)
    winners = db.Column(db.String(32))
    losers = db.Column(db.String(32))
    winning_score = db.column(db.Integer)
    losing_score = db.column(db.Integer)
    
    def __repr__(self):
        date_str = datetime.fromtimestamp(int(self.timestamp)).strftime("%Y-%m-%d %H:%M:%S")
        return "%s %02i:%02if %s:%s" % (date_str, self.winning_score, self.losing_score,
                                        self.winners, self.losers)

    
    
    
