from officepong import app, db, elo
from officepong.models import Player, Match
from flask import render_template, request, url_for
from time import time

@app.route('/provision')
def index():
    name = request.args.get('name', default=None)
    p = Player(name)
    db.session.add(p)
    db.session.commit()
    return redirect(url_for(''))

@app.route('/score')
def index():
    winners_str = request.args.get('winners')
    losers_str = request.args.get('losers')
    winning_score = request.args.get('winning_score', type=int)
    losing_score = request.args.get('losing_score', type=int)
    winning_names = winners_str.split(',')
    losing_names = losers_str.split(',')
    winning_elos = [db.session.query(Player).filter(User.name == name).first().elo
                   for name in winning_names]
    losing_elos = [db.session.query(Player).filter(User.name == name).first().elo
                   for name in losing_names]
    winning_elo = sum(winning_elos) / len(winning_elos)
    losing_elo = sum(losing_elos) / len(losing_elos)
    delta = elo.calculate_delta(winning_elo, losing_elo, winning_score, losing_score)

    m = Match(time(), winners, losers, winning_score, losing_score)
    db.session.add(m)
    for name, elo in zip(winning_names, winning_elos):
        db.session.query(Player).filter(name=name).update({Player.elo=elo})
    for name, elo in zip(losing_names, losing_elos):
        db.session.query(Player).filter(name=name).update({Player.elo=elo})
    db.session.commit()

    return redirect(url_for(''))

@app.route('/')
def index():
    matches = db.session.query(Match).all()
    players = db.session.query(Player).all()
    return render_template('home.html', matches=matches, players=players)
