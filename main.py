import os
import sys

import curl_cffi
from dotenv import load_dotenv

from load import load
from transform import transform


def fetch(url: str) -> str:
    response = curl_cffi.get(url)
    response.raise_for_status()
    return response.text


load_dotenv()
RANKINGS_URL = os.getenv("RANKINGS_URL")
POST_URL = os.getenv("POST_URL")


def main():
    # Check for missing environment variables and report all missing ones
    missing_vars = []
    if RANKINGS_URL is None:
        missing_vars.append("RANKINGS_URL")
    if POST_URL is None:
        missing_vars.append("POST_URL")

    if missing_vars:
        print(f"Missing required environment variables: {', '.join(missing_vars)}")
        sys.exit(1)

    try:
        html_response = fetch(RANKINGS_URL)  # type: ignore - RANKINGS_URL is checked above
    except Exception as e:
        print(f"Error fetching rankings from {RANKINGS_URL}: {e}")
        sys.exit(1)

    rankings = transform(html_response)
    load(POST_URL, rankings)  # type: ignore - POST_URL is checked above


if __name__ == "__main__":
    main()
