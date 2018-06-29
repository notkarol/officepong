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


@app.route('/add_match', methods=['POST'])
def add_match():
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
    winning_games = [db.session.query(Player).filter(Player.name == name).first().games
                    for name in winning_names]
    losing_games = [db.session.query(Player).filter(Player.name == name).first().games
                   for name in losing_names]
    winning_elo = sum(winning_elos) / len(winning_elos)
    losing_elo = sum(losing_elos) / len(losing_elos)
    actual, expected, delta = elo.calculate_delta(winning_elo, losing_elo,
                                                  winning_score, losing_score)
    match = Match(winners_str, losers_str, winning_score, losing_score, actual, expected, delta)
    db.session.add(match)
    for p_name, p_elo, p_games in zip(winning_names, winning_elos, winning_games):
        db.session.query(Player).filter_by(name=p_name).update({Player.elo: p_elo + delta,
                                                                Player.games: p_games + 1})
    for p_name, p_elo, p_games in zip(losing_names, losing_elos, losing_games):
        db.session.query(Player).filter_by(name=p_name).update({Player.elo: p_elo - delta,
                                                                Player.games: p_games + 1})
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/recalculate')
def recalculate():
    """
    Recalculate elo scores
    """
    #matches = db.session.query(Match).all()
    #players = db.session.query(Player).all()
    return redirect(url_for('index'))


@app.route('/')
def index():
    """
    The main page of the site. Display the dashboard.
    """
    def convert_timestamp(timestamp):
        return datetime.fromtimestamp(int(timestamp)).strftime("%m-%d")
    matches = db.session.query(Match).all()
    players = db.session.query(Player).all()
    players_list = sorted(((player.elo, player.name, player.games) for player in players), reverse=True)
    return render_template('home.html', matches=matches, players=players_list,
                           convert_timestamp=convert_timestamp)
