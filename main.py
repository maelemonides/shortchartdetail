import requests
import json
import pandas as pd

url_base = 'https://stats.nba.com/stats/shotchartdetail'

headers = {
		'Host': 'stats.nba.com',
		'Connection': 'keep-alive',
		'Accept': 'application/json, text/plain, */*',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
		'Referer': 'https://stats.nba.com/',
		"x-nba-stats-origin": "stats",
		"x-nba-stats-token": "true",
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'en-US,en;q=0.9',
	}

parameters = {
	'ContextMeasure': 'FGA',
	'LastNGames': 0,
	'LeagueID': '00',
	'Month': 0,
	'OpponentTeamID': 0,
	'Period': 0,
	'PlayerID': 201935,
	'SeasonType': 'Regular Season',
	'TeamID': 0,
	'VsDivision': '',
	'VsConference': '',
	'SeasonSegment': '',
	'Season': '2018-19',
	'RookieYear': '',
	'PlayerPosition': '',
	'Outcome': '',
	'Location': '',
	'GameSegment': '',
	'GameId': '',
	'DateTo': '',
	'DateFrom': ''
}


response = requests.get(url_base, params=parameters, headers=headers)
content = json.loads(response.content)

url_base = 'https://stats.nba.com/stats/shotchartdetail'
headers = {
		'Host': 'stats.nba.com',
		'Connection': 'keep-alive',
		'Accept': 'application/json, text/plain, */*',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
		'Referer': 'https://stats.nba.com/',
		"x-nba-stats-origin": "stats",
		"x-nba-stats-token": "true",
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'en-US,en;q=0.9',
	}

parameters = {
	'ContextMeasure': 'FGA',
	'LastNGames': 0,
	'LeagueID': '00',
	'Month': 0,
	'OpponentTeamID': 0,
	'Period': 0,
	'PlayerID': 201935,
	'SeasonType': 'Regular Season',
	'TeamID': 0,
	'VsDivision': '',
	'VsConference': '',
	'SeasonSegment': '',
	'Season': '2018-19',
	'RookieYear': '',
	'PlayerPosition': '',
	'Outcome': '',
	'Location': '',
	'GameSegment': '',
	'GameId': '',
	'DateTo': '',
	'DateFrom': ''
}

response = requests.get(url_base, params=parameters)
content = json.loads(response.content)

# transform contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df = pd.DataFrame(rows)
df.columns = headers

# write to csv file
df.to_csv('stats.csv', index=False)