#!/usr/bin/env python3
"""
Exercise 2 — Banner Grabbing & Service Fingerprinting
=====================================================

OBJECTIVE:
    Connect to each open port from Exercise 1 and figure out what
    service is running there by reading the "banner" — the first
    message a service sends when you connect.

WHAT YOU'LL LEARN:
    - How services identify themselves on the network
    - Reading data from sockets (recv)
    - The difference between services that send a banner immediately
      vs. services that wait for your input

INSTRUCTIONS:
    Fill in the TODO sections, then run:
        python ex2_banner_grabber.py

TIPS:
    - Some services send a banner as soon as you connect (FTP, Custom Protocol)
    - Some services wait for YOU to send something first (HTTP)
    - Set a short timeout so you don't hang on silent services
"""

import socket

# ─── Configuration ────────────────────────────────────────────────────

TARGET = "127.0.0.1"

# Paste the open ports you found in Exercise 1!
# (or keep this list — it will be revealed during the workshop)
OPEN_PORTS = []  # TODO: Fill in with the ports you discovered in Exercise 1

TIMEOUT = 3  # Seconds to wait for a banner

def grab_banner(host: str, port: int, timeout: float = TIMEOUT) -> str:
    """
    Connect to host:port and try to read the initial banner.

    Many services send a welcome message immediately after connection.
    If the service is silent, we send a generic probe and read the response.

    Returns:
        The banner/response as a string, or "[No banner]" if nothing was received.
    """

    # TODO: Create a TCP socket and set the timeout
    # TODO: Connect to (host, port)
    # TODO: Try to receive data (e.g., 1024 bytes)
    # TODO: If you received something, decode and return it
    # TODO: If the service was silent (timeout), try sending a probe:
    #       Send b"HEAD / HTTP/1.0\r\n\r\n" and read the response
    # TODO: Return the response or "[No banner]"
    # TODO: Handle exceptions gracefully

    pass  # Remove this line when you implement

def identify_service(port: int, banner: str) -> str:
    """
    Try to identify the service based on the banner content.

    Returns:
        A human-readable service name guess.
    """

    banner_lower = banner.lower()

    # TODO: Check the banner text for known service signatures
    # Examples:
    #   - FTP banners usually contain "ftp" or start with "220"
    #   - HTTP responses contain "HTTP/" or "html"
    #   - Custom services might have unique identifiers
    #
    # Return a string like "FTP", "HTTP", "Custom Protocol", "Unknown"

    pass  # Remove this line when you implement

# ─── Main ─────────────────────────────────────────────────────────────

def main():
    print("=" * 50)
    print("  Exercise 2: Banner Grabbing")
    print("=" * 50)
    print()

    if not OPEN_PORTS:
        print("⚠ OPEN_PORTS is empty!")
        print("  Fill it in with the ports from Exercise 1.")
        print("  Or run Exercise 1 first to discover them.")
        return

    results = []

    for port in OPEN_PORTS:
        print(f"─── Port {port} ───")
        banner = grab_banner(TARGET, port)
        service = identify_service(port, banner)

        # Show first 200 characters of the banner
        preview = banner[:200].replace("\n", "\\n")
        print(f"  Banner:  {preview}")
        print(f"  Service: {service}")
        print()

        results.append((port, service, banner))

    # Summary table
    print("═" * 50)
    print("  Service Map")
    print("═" * 50)
    for port, service, _ in results:
        print(f"  Port {port:>5}  →  {service}")

    print(f"\n💾 Now you know what's running! Time to interact with each service.")

if __name__ == "__main__":
    main()
