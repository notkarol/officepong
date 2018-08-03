import json
import urllib2
import os

def post(player1, player2, score1, score2, change):
    if (not os.path.isfile('./webhook.txt')): return
    data = {'text' : player1 + " beat " + player2 + "\n" + score1 + " to " + score2 + " for " + str(change) + " points"}

    req = urllib2.Request(open('webhook.txt').readline())
    req.add_header('Content-Type', 'application/json')

    response = urllib2.urlopen(req, json.dumps(data))

# post("Player1", "Player2", "21", "19", 4.5)
