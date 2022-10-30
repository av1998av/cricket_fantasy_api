import json
from flask import Flask, jsonify
import requests

app = Flask(__name__)

teams_data = [
	{"teamId" : 1, "name" : 'Visak'},
	{"teamId" : 2, "name" : 'Aadhi'},
	{"teamId" : 3, "name" : 'Hari'},
	{"teamId" : 4, "name" : 'Sankar'},
	{"teamId" : 5, "name" : 'Sivaguru'}
];

player_team_associations_data = [
    {'teamId': 1, 'playerId': 9782},
    {'teamId': 1, 'playerId': 60122},
    {'teamId': 1, 'playerId': 3852},
    {'teamId': 1, 'playerId': 28035},
    {'teamId': 1, 'playerId': 4255},
    {'teamId': 1, 'playerId': 65027},
    {'teamId': 1, 'playerId': 65027},
    {'teamId': 1, 'playerId': 63882},
    {'teamId': 1, 'playerId': 22878},
    {'teamId': 1, 'playerId': 67905},
    {'teamId': 1, 'playerId': 66046},
    {'teamId': 1, 'playerId': 4661},
    {'teamId': 1, 'playerId': 63881},
    {'teamId': 1, 'playerId': 74761},
    {'teamId': 1, 'playerId': 4321},
    {'teamId': 2, 'playerId': 11803},
    {'teamId': 2, 'playerId': 63940},
    {'teamId': 2, 'playerId': 10130},
    {'teamId': 2, 'playerId': 10085},
    {'teamId': 2, 'playerId': 65748},
    {'teamId': 2, 'playerId': 5313},
    {'teamId': 2, 'playerId': 4330},
    {'teamId': 2, 'playerId': 9844},
    {'teamId': 2, 'playerId': 59067},
    {'teamId': 2, 'playerId': 10172},
    {'teamId': 2, 'playerId': 57492},
    {'teamId': 2, 'playerId': 48191},
    {'teamId': 2, 'playerId': 4311},
    {'teamId': 2, 'playerId': 63206},
    {'teamId': 2, 'playerId': 57903},
    {'teamId': 3, 'playerId': 5380},
    {'teamId': 3, 'playerId': 10094},
    {'teamId': 3, 'playerId': 62576},
    {'teamId': 3, 'playerId': 4792},
    {'teamId': 3, 'playerId': 65739},
    {'teamId': 3, 'playerId': 65739},
    {'teamId': 3, 'playerId': 70326},
    {'teamId': 3, 'playerId': 65295},
    {'teamId': 3, 'playerId': 4357},
    {'teamId': 3, 'playerId': 63719},
    {'teamId': 3, 'playerId': 67927},
    {'teamId': 3, 'playerId': 65584},
    {'teamId': 3, 'playerId': 7797},
    {'teamId': 3, 'playerId': 67442},
    {'teamId': 3, 'playerId': 67519},
    {'teamId': 4, 'playerId': 20286},
    {'teamId': 4, 'playerId': 63751},
    {'teamId': 4, 'playerId': 13177},
    {'teamId': 4, 'playerId': 56964},
    {'teamId': 4, 'playerId': 4688},
    {'teamId': 4, 'playerId': 5132},
    {'teamId': 4, 'playerId': 66368},
    {'teamId': 4, 'playerId': 63641},
    {'teamId': 4, 'playerId': 67402},
    {'teamId': 4, 'playerId': 63875},
    {'teamId': 4, 'playerId': 4235},
    {'teamId': 4, 'playerId': 10183},
    {'teamId': 4, 'playerId': 3632},
    {'teamId': 4, 'playerId': 69956},
    {'teamId': 4, 'playerId': 26718},
    {'teamId': 5, 'playerId': 59429},
    {'teamId': 5, 'playerId': 3993},
    {'teamId': 5, 'playerId': 10053},
    {'teamId': 5, 'playerId': 66833},
    {'teamId': 5, 'playerId': 64219},
    {'teamId': 5, 'playerId': 63611},
    {'teamId': 5, 'playerId': 3782},
    {'teamId': 5, 'playerId': 4338},
    {'teamId': 5, 'playerId': 4196},
    {'teamId': 5, 'playerId': 57935},
    {'teamId': 5, 'playerId': 69274},
    {'teamId': 5, 'playerId': 5407},
    {'teamId': 5, 'playerId': 67717},
    {'teamId': 5, 'playerId': 25422},
    {'teamId': 5, 'playerId': 48607}
];

player_ids_data = [
    9782,
    60122,
    3852,
    28035,
    4255,
    65027,
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
    57492,
    57492,
    48191,
    4311,
    63206,
    57903,
    5380,
    10094,
    62576,
    4792,
    65739,
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
];

@app.route("/points")
def points():
	res = requests.get('https://icc.dream11.com/icc-season/services/feed/player/stats', 
	headers = {
		'Content-Type': 'application/json',
		'User-Agent': 'Mozilla/5.0',
		'Accept': '*/*',
		'Connection': 'keep-alive',
		'Accept-Encoding': 'gzip, deflate, br',
		'Sec-Fetch-Mode': 'cors',
		'Access-Control-Allow-Origin': '*'
	});
	if res.status_code == 200:
		return res.json()
	else:
		return jsonify({
			"message" : "server error"
		})

@app.route("/teams")
def teams():
	return jsonify(teams_data)

@app.route("/playerTeams")
def player_team_associations():
	return jsonify(player_team_associations_data)
	
@app.route("/playerIds")
def player_ids():
	return jsonify(player_ids_data)
		
if __name__ == "__main__":
    app.run(host='0.0.0.0')