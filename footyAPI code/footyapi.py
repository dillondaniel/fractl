import requests
import json
import csv
from time import sleep

api_url = ("https://api.football-data-api.com/league-matches?key=********&season_id=5862")
response = requests.get(api_url)
x = response.json()

with open ('CA-21.csv', 'x', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(['Year','Home','Away','Home Goals','Away Goals','Home Yellows','Away Yellows','Home Reds','Away Reds','Home Fouls','Away Fouls', 'Referee'])

    for y in range(len(x['data'])):

        year = (x['data'][y]['season'])
        home = (x['data'][y]['home_name'])
        away = (x['data'][y]['away_name'])
        home_score = (x['data'][y]['homeGoalCount'])
        away_score = (x['data'][y]['awayGoalCount'])
        home_yellow_cards = (x['data'][y]['team_a_yellow_cards'])
        away_yellow_cards = (x['data'][y]['team_b_yellow_cards'])
        home_red_cards = (x['data'][y]['team_a_red_cards'])
        away_red_cards = (x['data'][y]['team_b_red_cards'])
        home_fouls_called = (x['data'][y]['team_a_fouls'])
        away_fouls_called = (x['data'][y]['team_b_fouls'])
        referee = (x['data'][y]['refereeID'])
        if referee == None:
            ref_name = 'No data to collect'
        else:
            ref_url = 'https://api.football-data-api.com/referee?key=pattystats&referee_id='+str(referee)
            reponse2 = requests.get(ref_url)
            r = reponse2.json()
            ref_name = (r['data'][0]['full_name'])
        row_store = [year,home,away,home_score,away_score,home_yellow_cards,away_yellow_cards,home_red_cards,away_red_cards,home_fouls_called,away_fouls_called,ref_name]
        writer.writerow(row_store)
