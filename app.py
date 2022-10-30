import json
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
cors = CORS(app)

player_team_associations_data = [
    {'teamId': 0, 'playerId': 9782},
    {'teamId': 0, 'playerId': 60122},
    {'teamId': 0, 'playerId': 3852},
    {'teamId': 0, 'playerId': 28035},
    {'teamId': 0, 'playerId': 4255},
    {'teamId': 0, 'playerId': 65027},
    {'teamId': 0, 'playerId': 58913},
    {'teamId': 0, 'playerId': 63882},
    {'teamId': 0, 'playerId': 22878},
    {'teamId': 0, 'playerId': 67905},
    {'teamId': 0, 'playerId': 66046},
    {'teamId': 0, 'playerId': 4661},
    {'teamId': 0, 'playerId': 63881},
    {'teamId': 0, 'playerId': 74761},
    {'teamId': 0, 'playerId': 4321},
    {'teamId': 1, 'playerId': 11803},
    {'teamId': 1, 'playerId': 63940},
    {'teamId': 1, 'playerId': 10130},
    {'teamId': 1, 'playerId': 10085},
    {'teamId': 1, 'playerId': 65748},
    {'teamId': 1, 'playerId': 5313},
    {'teamId': 1, 'playerId': 4330},
    {'teamId': 1, 'playerId': 9844},
    {'teamId': 1, 'playerId': 59067},
    {'teamId': 1, 'playerId': 10172},
    {'teamId': 1, 'playerId': 57492},
    {'teamId': 1, 'playerId': 48191},
    {'teamId': 1, 'playerId': 4311},
    {'teamId': 1, 'playerId': 63206},
    {'teamId': 1, 'playerId': 57903},
    {'teamId': 2, 'playerId': 5380},
    {'teamId': 2, 'playerId': 10094},
    {'teamId': 2, 'playerId': 62576},
    {'teamId': 2, 'playerId': 4792},
    {'teamId': 2, 'playerId': 57871},
    {'teamId': 2, 'playerId': 65739},
    {'teamId': 2, 'playerId': 70326},
    {'teamId': 2, 'playerId': 65295},
    {'teamId': 2, 'playerId': 4357},
    {'teamId': 2, 'playerId': 63719},
    {'teamId': 2, 'playerId': 67927},
    {'teamId': 2, 'playerId': 65584},
    {'teamId': 2, 'playerId': 7797},
    {'teamId': 2, 'playerId': 67442},
    {'teamId': 2, 'playerId': 67519},
    {'teamId': 3, 'playerId': 20286},
    {'teamId': 3, 'playerId': 63751},
    {'teamId': 3, 'playerId': 13177},
    {'teamId': 3, 'playerId': 56964},
    {'teamId': 3, 'playerId': 4688},
    {'teamId': 3, 'playerId': 5132},
    {'teamId': 3, 'playerId': 66368},
    {'teamId': 3, 'playerId': 63641},
    {'teamId': 3, 'playerId': 67402},
    {'teamId': 3, 'playerId': 63875},
    {'teamId': 3, 'playerId': 4235},
    {'teamId': 3, 'playerId': 10183},
    {'teamId': 3, 'playerId': 3632},
    {'teamId': 3, 'playerId': 69956},
    {'teamId': 3, 'playerId': 26718},
    {'teamId': 4, 'playerId': 59429},
    {'teamId': 4, 'playerId': 3993},
    {'teamId': 4, 'playerId': 10053},
    {'teamId': 4, 'playerId': 66833},
    {'teamId': 4, 'playerId': 64219},
    {'teamId': 4, 'playerId': 63611},
    {'teamId': 4, 'playerId': 3782},
    {'teamId': 4, 'playerId': 4338},
    {'teamId': 4, 'playerId': 4196},
    {'teamId': 4, 'playerId': 57935},
    {'teamId': 4, 'playerId': 69274},
    {'teamId': 4, 'playerId': 5407},
    {'teamId': 4, 'playerId': 67717},
    {'teamId': 4, 'playerId': 25422},
    {'teamId': 4, 'playerId': 48607}
]

player_ids_data = [
    9782,
    60122,
    3852,
    28035,
    4255,
    58913,
    65027,
    63882,
    22878,
    67905,
    66046,
    4661,
    63881,
    74761,
    4321,
    11803,
    63940,
    10130,
    10085,
    65748,
    5313,
    4330,
    9844,
    59067,
    10172,
    57492,
    48191,
    4311,
    63206,
    57903,
    5380,
    10094,
    62576,
    4792,
    57871,
    65739,
    70326,
    65295,
    4357,
    63719,
    67927,
    65584,
    7797,
    67442,
    67519,
    20286,
    63751,
    13177,
    56964,
    4688,
    5132,
    66368,
    63641,
    67402,
    63875,
    4235,
    10183,
    3632,
    69956,
    26718,
    59429,
    3993,
    10053,
    66833,
    64219,
    63611,
    3782,
    4338,
    4196,
    57935,
    69274,
    5407,
    67717,
    25422,
    48607
]

@app.route("/")
def points():
	teams_data = [
        {"name" : 'Visak','players' : [], 'points' : 0},
        {"name" : 'Aadhi','players' : [], 'points' : 0},
        {"name" : 'Hari','players' : [], 'points' : 0},
        {"name" : 'Sankar','players' : [], 'points' : 0},
        {"name" : 'Sivaguru','players' : [], 'points' : 0}
    ]
	res = requests.get('https://icc.dream11.com/icc-season/services/feed/player/stats', 
	headers = {
		'Content-Type': 'application/json',
		'User-Agent': 'Mozilla/5.0',
		'Accept': '*/*',
		'Connection': 'keep-alive',
		'Accept-Encoding': 'gzip, deflate, br',
		'Sec-Fetch-Mode': 'cors',
		'Access-Control-Allow-Origin': '*'
	})
	if res.status_code == 200:
		for player in json.loads(res.text)['Data']['Value']['PlayerStats']:
			if player['plyrid'] in player_ids_data:
				team_id = [x['teamId'] for x in player_team_associations_data if x['playerId'] == player['plyrid']][0]
				teams_data[team_id]['players'].append({
				    'playerId' : player['plyrid'],
				    'playerName' : player['plyrnm'],
				    'points' : int(player['ovrpoint'])
 				})
				teams_data[team_id]['points'] += int(player['ovrpoint'])
		return json.dumps(teams_data)
	else:
	    return jsonify({
			"message" : "server error"
        })
    
		
if __name__ == "__main__":
    app.run(host='0.0.0.0')