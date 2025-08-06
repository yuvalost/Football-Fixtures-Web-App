import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

LEAGUES = {
    "PL": "Premier League",
    "PD": "La Liga",
    "SA": "Serie A"
}

CACHE = {"data": None, "last_updated": 0}

def get_fixtures():
    now = time.time()

    if CACHE["data"] and (now - CACHE["last_updated"] < 1200):  # 20 minutes
        return CACHE["data"]

    api_key = os.getenv("FOOTBALL_API_KEY")
    if not api_key:
        raise EnvironmentError("Missing FOOTBALL_API_KEY")

    headers = {"X-Auth-Token": api_key}
    all_fixtures = {}

    for code, name in LEAGUES.items():
        url = f"https://api.football-data.org/v4/competitions/{code}/matches?status=SCHEDULED"
        try:
            res = requests.get(url, headers=headers)
            res.raise_for_status()
            all_fixtures[name] = res.json()["matches"]
        except requests.RequestException as e:
            print(f"Error fetching {name}: {e}")
            all_fixtures[name] = []

    CACHE["data"] = all_fixtures
    CACHE["last_updated"] = now
    return all_fixtures
