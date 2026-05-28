#!/usr/bin/env python3
"""
Exercise 7 — Admin Gate: The Final Challenge
=============================================

OBJECTIVE:
    Use pwntools to connect to the Admin Gate and submit all 4 secrets
    you've collected to capture the flag!

WHAT YOU'LL LEARN:
    - Combining all the secrets from previous exercises
    - Precise protocol interaction with pwntools
    - The satisfaction of solving a multi-stage challenge!

BACKSTORY:
    You've explored every service on the Mystery Machine:
      - SECRET_1 from FTP     (Exercise 3)
      - SECRET_2 from HTTP    (Exercise 4)
      - SECRET_3 from DNS     (Exercise 5)
      - SECRET_4 from Custom  (Exercise 6)

    One service remains: the Admin Gate. It requires all 4 secrets
    to unlock the final flag.

INSTRUCTIONS:
    Fill in your secrets and the TODO sections, then run:
        python ex7_admin_gate.py
"""

from pwn import remote, context

# Suppress pwntools' verbose banners
context.log_level = "error"

# ─── Configuration ────────────────────────────────────────────────────

TARGET = "127.0.0.1"
ADMIN_PORT = None  # TODO: Fill in the Admin Gate port you discovered

# Fill in the secrets you've collected!
SECRETS = {
    "SECRET_1": "",  # TODO: From FTP (Exercise 3)
    "SECRET_2": "",  # TODO: From HTTP (Exercise 4)
    "SECRET_3": "",  # TODO: From DNS (Exercise 5)
    "SECRET_4": "",  # TODO: From Custom Protocol (Exercise 6)
}

def capture_the_flag(host: str, port: int, secrets: dict) -> str | None:
    """
    Connect to the Admin Gate and submit all secrets to get the flag.

    The Admin Gate protocol:
      1. Shows a banner and lists missing secrets
      2. Prompts "Enter secret> " for each submission
      3. Accepts format: KEY=VALUE
      4. After all 4 are submitted, reveals the flag

    Returns:
        The flag string if successful, None otherwise.
    """

    # TODO: Connect to the Admin Gate with pwntools
    # TODO: Read the banner

    # TODO: For each secret in our collection:
    #   - Wait for the "Enter secret> " prompt
    #   - Send the secret in KEY=VALUE format
    #   - Read the response to confirm it was accepted

    # TODO: After all secrets are submitted, read the final response
    # TODO: Extract the final token returned by the service

    # TODO: Close the connection and return the flag

    pass  # Remove when you implement

# ─── Main ─────────────────────────────────────────────────────────────

def main():
    print("=" * 50)
    print("  Exercise 7: Admin Gate — Final Challenge")
    print("=" * 50)
    print()

    # Check that all secrets are filled in
    missing = [k for k, v in SECRETS.items() if not v]
    if missing:
        print("⚠ You haven't filled in all the secrets yet!")
        print(f"  Missing: {', '.join(missing)}")
        print("  Go back and complete the previous exercises first.")
        print()
        print("  Or... try to solve it anyway with what you have!")
        if all(not v for v in SECRETS.values()):
            return

    print("Secrets collected:")
    for key, value in SECRETS.items():
        status = "✓" if value else "✗"
        display = value if value else "(missing)"
        print(f"  {status} {key} = {display}")
    print()

    flag = capture_the_flag(TARGET, ADMIN_PORT, SECRETS)

    if flag:
        print(f"\n🏆 FLAG CAPTURED: {flag}")
        print("\n🎉 Congratulations! You've completed the workshop!")
        print("   You built your own scanner, explored unknown services,")
        print("   and conquered the Mystery Machine — all with Python!")
    else:
        print("\n⚠ Didn't capture the flag.")
        print("  Double-check your secrets and try again!")

if __name__ == "__main__":
    main()
