import requests

data = requests.get("http://localhost:5000/fixtures").json()

for league, matches in data.items():
    print(f"\n=== {league} ===")
    for match in matches:
        home = match['homeTeam']['name']
        away = match['awayTeam']['name']
        date = match['utcDate']
        print(f"{home} vs {away} on {date}")
