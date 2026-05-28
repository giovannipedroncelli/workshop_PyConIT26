#!/usr/bin/env python3
"""
Exercise 4 — HTTP Detective
============================

OBJECTIVE:
    Investigate the HTTP service, find hidden endpoints, and extract SECRET_2.

WHAT YOU'LL LEARN:
    - Making HTTP requests with Python (urllib and requests)
    - Reading HTTP response headers for clues
    - The importance of robots.txt in reconnaissance
    - How HTTP headers influence server behavior

BACKSTORY:
    Your banner grab revealed a web server. Web services often hide
    interesting things behind standard conventions and metadata.
    Time to think like a web detective!

INSTRUCTIONS:
    Fill in the TODO sections in main(), then run:
        python ex4_http_detective.py
"""

import json
import socket
import urllib.error
import urllib.request

try:
    import requests
except ImportError:  # pragma: no cover
    requests = None

# ─── Configuration ────────────────────────────────────────────────────

TARGET = "127.0.0.1"
HTTP_PORT = None  # TODO: Fill in the HTTP port you discovered
BASE_URL = f"http://{TARGET}:{HTTP_PORT}"
TIMEOUT = 5

def http_get(client: str, url: str, headers: dict[str, str] | None = None) -> dict:
    """HTTP GET helper used by the exercise flow in main()."""
    headers = headers or {}

    if client == "urllib":
        request = urllib.request.Request(url, headers=headers)
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        try:
            with opener.open(request, timeout=TIMEOUT) as response:
                return {
                    "status": response.status,
                    "headers": dict(response.getheaders()),
                    "text": response.read().decode("utf-8", errors="replace"),
                }
        except urllib.error.HTTPError as error:
            return {
                "status": error.code,
                "headers": dict(error.headers.items()),
                "text": error.read().decode("utf-8", errors="replace"),
            }
        except (urllib.error.URLError, TimeoutError, socket.timeout) as error:
            return {"status": 0, "headers": {}, "text": f"Network error: {error}"}

    try:
        with requests.Session() as session:
            session.trust_env = False
            merged_headers = {"Connection": "close"}
            merged_headers.update(headers)
            response = session.get(url, headers=merged_headers, timeout=(3, TIMEOUT))
            return {
                "status": response.status_code,
                "headers": dict(response.headers),
                "text": response.text,
            }
    except requests.RequestException as error:
        return {"status": 0, "headers": {}, "text": f"Network error: {error}"}

# ─── Main ─────────────────────────────────────────────────────────────

def main():
    print("=" * 50)
    print("  Exercise 4: HTTP Detective")
    print("=" * 50)
    print()

    # You can switch this to "requests" if installed.
    client = "urllib"
    if requests is not None:
        print("[Info] requests is available. You can switch client = \"requests\".")

    # STEP 1: GET /
    # TODO: call http_get(client, f"{BASE_URL}/")
    # TODO: print status code
    # TODO: print headers
    # TODO: print first 200 chars of body

    # STEP 2: GET /robots.txt
    # TODO: call http_get(client, f"{BASE_URL}/robots.txt")
    # TODO: print robots.txt content
    # TODO: parse line starting with "Disallow:" to extract hidden_path

    # STEP 3: GET hidden_path, then retry with User-Agent
    # TODO: call http_get(client, f"{BASE_URL}{hidden_path}") with default headers
    # TODO: parse JSON response and inspect hint/domain
    # TODO: call again with headers={"User-Agent": "PyCon-Scanner"}
    # TODO: parse JSON and print SECRET_2

    pass  # Remove when you implement the flow above

if __name__ == "__main__":
    main()
