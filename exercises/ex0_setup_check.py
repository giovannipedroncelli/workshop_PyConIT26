#!/usr/bin/env python3
"""
Exercise 0 — Setup Check
=========================
Run this script to verify that your Python environment is ready
and that the Mystery Machine target is alive.

Usage:
    python ex0_setup_check.py
"""

import socket
import sys

TARGET = "127.0.0.1"
EXPECTED_TCP_PORTS = [2121, 8080, 9999, 4444]

def check_packages():
    """Check that required Python packages are installed."""
    packages = {
        "pwntools": "pwn",
        "dnspython": "dns",
        "requests": "requests",
    }
    all_ok = True
    for name, import_name in packages.items():
        try:
            __import__(import_name)
            print(f"  [OK] {name}")
        except ImportError:
            print(f"  [MISSING] {name} — install with: pip install {name}")
            all_ok = False
    return all_ok

def check_target_alive(host, timeout=0.8):
    """
    Quick setup health-check for known Mystery Machine services.

    Returns True if at least one expected service is reachable.
    """
    def check_tcp(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                return s.connect_ex((host, port)) == 0
        except OSError:
            return False

    return any(check_tcp(port) for port in EXPECTED_TCP_PORTS)

def main():
    print("=" * 50)
    print("  Workshop Setup Check")
    print("=" * 50)
    print()

    # Check Python version
    print(f"Python version: {sys.version}")
    if sys.version_info < (3, 10):
        print("  [WARNING] Python 3.10+ is recommended")
    else:
        print("  [OK] Python version")
    print()

    # Check packages
    print("Checking Python packages:")
    packages_ok = check_packages()
    print()

    # Check target is reachable
    print("Checking Mystery Machine target:")
    print(f"  Checking if the target is alive on {TARGET}...")
    target_ok = check_target_alive(TARGET)

    if target_ok:
        print("  [OK] The Mystery Machine is alive! Something is listening.")
        print("       What services are running? That's for YOU to discover.")
    else:
        print("  [DOWN] No expected services detected on the target.")
        print("         Ask the instructor to start the Mystery Machine.")
    print()

    # Summary
    if packages_ok and target_ok:
        print("All systems go! You're ready for the workshop.")
        print("Start with ex1_port_scanner.py to discover what's out there.")
    else:
        if not target_ok:
            print("The Mystery Machine doesn't seem to be running.")
            print("Ask the instructor for help.")
        if not packages_ok:
            print("Some packages are missing.")
            print("Run: pip install -r ../requirements.txt")

if __name__ == "__main__":
    main()
