# officepong

Your office plays ping pong (or foosball) and some people just won't shut up about how they won a match last week. You sort of remember it happening, but more clearly remember beating them 4 games in a row. It might be their turn to gloat, but you want some talking points too.

That's where OfficePong comes in. Set it up on someone's computer (or the cloud) and record all your games. It's simple to use from a phone, tablet, or laptop. Behind the scenes it grades matches using an aggressively-tuned ELO system. Whoever is on top today won't be there for long. Like playing doubles? Well we fudged some math so you can include those clown fiestas too. Since it ranks matches based on the score, even novices can get their revenge by gaining ELO on a lost game. If you don't see your score immediately on the leaderboard, don't worry. There's a 3 game minimum before it show up.

![example of web site](https://raw.githubusercontent.com/notkarol/officepong/master/officepong.png)

## Install

This is a basic python-based Flask webapp. While it has been developed and used primarily on Ubuntu Linux, any Linux machine will work. In the future I'll probably get around to setting up instructions for a cloud instance. It's self-contained, with a local database, but as there's no credentialing or write limitations, I recommend you keep it available only inside your local network.

```bash
sudo apt install python3-pip sqlite3
pip3 install --user flask flask_sqlalchemy
cat officepong.sql | sqlite3 /tmp/officepong.db
python3 setup.py install --user
```

## Run

```bash
FLASK_APP=officepong nohup flask run --host 0.0.0.0 &
```

Navigate to http://localhost:5000/ in your browser. Nohup allows it to continue running after you close your terminal window.

If you need to delete or change a player or score please do that directly through the database. Otherwise, you can do the following actions in the browser. The database is a basic sqlite instance with two tables (player and match). If you ever delete a match or update one's scores, click the Recalculate button on the website and it will automatically correct every player's ELO, games played, and non-score statistics in the matches.

If you need to rename a player, good luck.

## Update

If a new version ever comes out, you can install and run it using the following:

```bash
cd officepong
git pull
python3 setup.py install --user
killall flask
FLASK_APP=officepong nohup flask run --host 0.0.0.0 &
```
