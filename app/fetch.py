import requests
import os
import time

CACHE = {"data": None, "last_updated": 0}
LEAGUES = {"PL": "Premier League", "PD": "La Liga", "SA": "Serie A"}

def get_fixtures():
    now = time.time()
    if CACHE["data"] and (now - CACHE["last_updated"] < 1200):  # 20 mins
        return CACHE["data"]

    headers = {"X-Auth-Token": os.getenv("FOOTBALL_API_KEY")}
    all_fixtures = {}

    for code, name in LEAGUES.items():
        url = f"https://api.football-data.org/v4/competitions/{code}/matches?status=SCHEDULED"
        res = requests.get(url, headers=headers)
        if res.ok:
            all_fixtures[name] = res.json()["matches"]

    CACHE["data"] = all_fixtures
    CACHE["last_updated"] = now
    return all_fixtures
