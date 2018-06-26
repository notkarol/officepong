"""
Handle routes for Flask website
"""
from datetime import datetime
from flask import redirect, render_template, request, url_for

from officepong import app, db, elo
from officepong.models import Player, Match

@app.route('/register', methods=['POST'])
def register():
    """ Register a new user by adding them to the database. """
    name = request.form['name']
    player = Player(name)
    db.session.add(player)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/score', methods=['POST'])
def score():
    """
    Store the result of the match in the database and update the players'
    elo scores.
    """
    winning_names = request.form.getlist('winner')
    losing_names = request.form.getlist('loser')
    winners_str = ','.join(winning_names)
    losers_str = ','.join(losing_names)
    winning_score = int(request.form['winning_score'])
    losing_score = int(request.form['losing_score'])
    winning_elos = [db.session.query(Player).filter(Player.name == name).first().elo
                    for name in winning_names]
    losing_elos = [db.session.query(Player).filter(Player.name == name).first().elo
                   for name in losing_names]
    winning_elo = sum(winning_elos) / len(winning_elos)
    losing_elo = sum(losing_elos) / len(losing_elos)
    delta, expected = elo.calculate_delta(winning_elo, losing_elo, winning_score, losing_score)
    match = Match(winners_str, losers_str, winning_score, losing_score, expected)
    db.session.add(match)
    for p_name, p_elo in zip(winning_names, winning_elos):
        db.session.query(Player).filter_by(name=p_name).update({Player.elo: p_elo + delta})
    for p_name, p_elo in zip(losing_names, losing_elos):
        db.session.query(Player).filter_by(name=p_name).update({Player.elo: p_elo - delta})
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/')
def index():
    """
    The main page of the site. Display the dashboard.
    """
    def convert_timestamp(timestamp):
        return datetime.fromtimestamp(int(timestamp)).strftime("%m-%d %H:%M")
    matches = db.session.query(Match).all()
    players = db.session.query(Player).all()
    players_list = sorted(((player.elo, player.name) for player in players), reverse=True)
    return render_template('home.html', matches=matches, players=players_list,
                           convert_timestamp=convert_timestamp)
