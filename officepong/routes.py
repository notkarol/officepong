"""
Handle routes for Flask website
"""
from datetime import datetime
from flask import redirect, render_template, request, url_for

from officepong import app, db, elo, slack
from officepong.models import Player, Match

@app.route('/register', methods=['POST'])
def register():
    """ Register a new user by adding them to the database. """
    name = request.form['name']
    if not len(name):
        return redirect(url_for('index'))
    db.session.add(Player(name))
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/add_match', methods=['POST'])
def add_match():
    """
    Store the result of the match in the database and update the players'
    elo scores.
    """

    # Extract fields from request fields
    win_names, lose_names = request.form.getlist('winner'), request.form.getlist('loser')
    win_score, lose_score = int(request.form['win_score']), int(request.form['lose_score'])

    # Minimize misclicks
    if lose_score + 2 > win_score or (win_score not in (11, 21) and lose_score + 2 != win_score):
        return redirect(url_for('index'))

    # Don't add score if there's a problem with the names
    if not win_names or not lose_names:
        return redirect(url_for('index'))
    for name in win_names:
        if name in lose_names:
            return redirect(url_for('index'))
    for name in lose_names:
        if name in win_names:
            return redirect(url_for('index'))

    # Map each player to their current elo and #games for easy use below
    players = {}
    for player in db.session.query(Player).all():
        players[player.name] = {'elo': player.elo, 'games': player.games}

    # Figure out the elo and its change for the players
    win_elo = sum([players[name]['elo'] for name in win_names])
    lose_elo = sum([players[name]['elo'] for name in lose_names])
    actual, expected, delta = elo.calculate_delta(win_elo, lose_elo, win_score, lose_score)

    # Update elo and #games for both losers and winners
    for name in win_names:
        e = players[name]['elo'] + delta / len(win_names)
        g = players[name]['games'] + 1
        db.session.query(Player).filter_by(name=name).update({Player.elo: e, Player.games: g})
    for name in lose_names:
        e = players[name]['elo'] - delta / len(lose_names)
        g = players[name]['games'] + 1
        db.session.query(Player).filter_by(name=name).update({Player.elo: e, Player.games: g})

    # Add match to database
    win_str, lose_str = ','.join(win_names), ','.join(lose_names)
    match = Match(win_str, lose_str, win_score, lose_score, actual, expected, delta)
    db.session.add(match)

    db.session.commit()
    slack.post(win_names, lose_names, win_score, lose_score, delta)
    return redirect(url_for('index'))


@app.route('/recalculate', methods=['POST'])
def recalculate():
    """
    Recalculate elo scores
    """
    # Get the initialization of every player in the database
    players = {}
    for player in db.session.query(Player).all():
        players[player.name] = {'elo': Player.elo.default.arg, 'games': Player.games.default.arg}


    # Update eatch match
    for match in db.session.query(Match).order_by(Match.timestamp).all():
        winners = match.winners.split(',')
        losers = match.losers.split(',')
        win_elo = sum([players[name]['elo'] for name in winners])
        lose_elo = sum([players[name]['elo'] for name in losers])
        actual, expected, delta = elo.calculate_delta(win_elo, lose_elo,
                                                      match.win_score, match.lose_score)

        # Update player totals
        for name in winners:
            players[name]['elo'] += delta / len(winners)
            players[name]['games'] += 1
        for name in losers:
            players[name]['elo'] -= delta / len(losers)
            players[name]['games'] += 1

        # Submit match
        args = {Match.actual: actual, Match.expected: expected, Match.delta: delta}
        db.session.query(Match).filter_by(timestamp=match.timestamp).update(args)

    # Update each player's elo and # of games played
    for name in players:
        args = {Player.elo: players[name]['elo'], Player.games: players[name]['games']}
        db.session.query(Player).filter_by(name=name).update(args)

    db.session.commit()
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
    players_list = sorted(((player.elo, player.name, player.games) for player in players),
                          reverse=True)
    return render_template('home.html', matches=matches, players=players_list,
                           convert_timestamp=convert_timestamp)
