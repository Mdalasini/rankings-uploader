# Rankings Uploader

A Python script that fetches football rankings from a website, transforms the data, and uploads it to an API.

## Setup

1. Install dependencies with uv:
   ```bash
   uv sync
   ```

2. Set environment variables:
   ```bash
   export RANKINGS_URL="https://example.com/rankings"
   export POST_URL="https://api.example.com/rankings"
   ```

3. Run the script:
   ```bash
   uv run python main.py
   ```

## GitHub Actions

The script runs automatically every day at midnight UTC via GitHub Actions. 

To enable:
1. Add `RANKINGS_URL` and `POST_URL` to your repository's Secrets
2. Push to GitHub

## Dependencies

- curl-cffi: HTTP requests
- python-dotenv: Environment variable management  
- selectolax: HTML parsing