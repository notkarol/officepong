# officepong

![example of web site](https://raw.githubusercontent.com/notkarol/officepong/master/officepong.png)

## Install

Expect that you have Ubuntu 16.04+ installed.

```bash
sudo apt install python3-pip sqlite3
pip3 install --user flask flask_sqlalchemy
cat officepong.sql | sqlite3 /tmp/officepong.db
python3 setup.py install --user
```

## Run

```bash
FLASK_APP=officepong flask run --host 0.0.0.0
```

Navigate to http://localhost:5000/ in your browser. 


## Usage

If you need to delete or change a player or score please do that directly through the database. Otherwise, you can do the following actions in the browser.

* Add Match
* Add Player
* Recalculate (after any changes to database)
