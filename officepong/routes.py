from officepong import app, db, elo
from officepong.forms import RegisterForm, ScoreForm
from officepong.models import Player, Match
from flask import redirect, render_template, request, url_for

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    p = Player(name)
    db.session.add(p)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/score', methods=['POST'])
def score():
    print(request.form)
    winners_str = request.form['winners_str']
    losers_str = request.form['losers_str']
    winning_score = int(request.form['winning_score'])
    losing_score = int(request.form['losing_score'])
    winning_names = winners_str.split(',')
    losing_names = losers_str.split(',')
    winning_elos = [db.session.query(Player).filter(Player.name == name).first().elo
                   for name in winning_names]
    losing_elos = [db.session.query(Player).filter(Player.name == name).first().elo
                   for name in losing_names]
    winning_elo = sum(winning_elos) / len(winning_elos)
    losing_elo = sum(losing_elos) / len(losing_elos)
    delta = elo.calculate_delta(winning_elo, losing_elo, winning_score, losing_score)

    m = Match(winners_str, losers_str, winning_score, losing_score)
    db.session.add(m)
    for p_name, p_elo in zip(winning_names, winning_elos):
        db.session.query(Player).filter_by(name=p_name).update({Player.elo: p_elo})
    for p_name, p_elo in zip(losing_names, losing_elos):
        db.session.query(Player).filter_by(name=p_name).update({Player.elo: p_elo})
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/')
def index():
    register_form = RegisterForm()
    score_form = ScoreForm()
    matches = db.session.query(Match).all()
    players = db.session.query(Player).all()
    return render_template('home.html', matches=matches, players=players,
                           register_form=register_form, score_form=score_form)
