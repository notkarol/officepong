# officepong

## Install

Expect that you have Ubuntu 16.04+ installed.

```bash
sudo apt install python3-flask
cat officepong.sql | sqlite3 /tmp/officepong.db
python3 setup.py install --user
```

## Run

```bash
FLASK_APP=officepong flask run
```

Navigate to [http://127.0.0.1:5000/] in your browser. 
