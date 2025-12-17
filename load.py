import os
import sys

import curl_cffi
from dotenv import load_dotenv

from models import Team

load_dotenv()
POST_URL = os.getenv("POST_URL")


team_name_to_id = {
    "Arsenal": 1,
    "Aston Villa": 2,
    "Bournemouth": 3,
    "Brentford": 4,
    "Brighton and Hove": 5,
    "Burnley": 6,
    "Chelsea": 7,
    "Crystal Palace": 8,
    "Everton": 9,
    "Fulham": 10,
    "Leeds United": 11,
    "Liverpool": 12,
    "Manchester City": 13,
    "Manchester United": 14,
    "Newcastle United": 15,
    "Nottingham Forest": 16,
    "Sunderland": 17,
    "Tottenham Hotspur": 18,
    "West Ham United": 19,
    "Wolverhampton Wanderers": 20,
}


def load(url: str, teams: list[Team]):
    # Build payload, catching missing team names
    try:
        payload = [
            {
                "team_id": team_name_to_id[team.team_name],
                "off_rank": team.off_rank,
                "def_rank": team.def_rank,
            }
            for team in teams
        ]
    except KeyError as missing:
        print(f"Unknown team name: {missing}", file=sys.stderr)
        sys.exit(1)

    # POST it
    try:
        curl_cffi.post(url, json=payload)
    except Exception as post_err:  # network, timeout, etc.
        print(f"POST failed: {post_err}", file=sys.stderr)
        sys.exit(1)
