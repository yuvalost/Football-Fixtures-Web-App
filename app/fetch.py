import os
import time
import requests
from dotenv import load_dotenv

# Load environment variables from .env file (only needed for local dev)
load_dotenv()

# Constants
LEAGUES = {
    "PL": "Premier League",
    "PD": "La Liga",
    "SA": "Serie A"
}

CACHE = {"data": None, "last_updated": 0}

def get_fixtures():
    now = time.time()

    # Use cached data if fresh
    if CACHE["data"] and (now - CACHE["last_updated"] < 1200):  # 20 mins
        return CACHE["data"]

    # Load API key
    api_key = os.getenv("FOOTBALL_API_KEY")
    if not api_key:
        raise ValueError("Missing FOOTBALL_API_KEY in environment variables")

    headers = {"X-Auth-Token": api_key}
    all_fixtures = {}

    for code, name in LEAGUES.items():
        url = f"https://api.football-data.org/v4/competitions/{code}/matches?status=SCHEDULED"
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            all_fixtures[name] = response.json()["matches"]
        except requests.RequestException as e:
            print(f"Error fetching {name} fixtures: {e}")
            all_fixtures[name] = []

    # Cache results
    CACHE["data"] = all_fixtures
    CACHE["last_updated"] = now
    return all_fixtures
