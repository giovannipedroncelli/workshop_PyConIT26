#!/usr/bin/env python3
"""
Exercise 6 — Custom Protocol Hacker (with pwntools!)
=====================================================

OBJECTIVE:
    Interact with the custom protocol service to solve a challenge and
    extract SECRET_4. This is where we introduce pwntools!

WHAT YOU'LL LEARN:
    - pwntools basics: remote(), sendline(), recvline(), recvuntil()
    - Interacting with custom (non-standard) network protocols
    - Decoding challenges (Base64) programmatically
    - Why pwntools is the go-to tool for protocol interaction

BACKSTORY:
    Your banner grabber found a custom text-based protocol on one of the
    ports. The banner mentioned something about a HELP command...
    Time to speak its language!

WHAT IS PWNTOOLS?
    pwntools is a Python library designed for rapid prototyping
    of exploits and network interactions. Key features:
      - remote(host, port): connect to a TCP service
      - r.sendline(b"cmd"): send a command + newline
      - r.recvline(): read one line
      - r.recvuntil(b">"): read until a delimiter
      - r.interactive(): drop into manual mode

INSTRUCTIONS:
    Fill in the TODO sections, then run:
        python ex6_protocol_hacker.py
"""

import base64  # noqa: you'll discover why you need this!
from pwn import remote, context

# Suppress pwntools' verbose banners
context.log_level = "error"

# ─── Configuration ────────────────────────────────────────────────────

TARGET = "127.0.0.1"
PORT = None  # TODO: Fill in the custom protocol port you discovered

def interact_with_service(host: str, port: int) -> str | None:
    """
    Connect to the custom protocol service, explore its commands,
    and retrieve SECRET_4.

    Start by reading the banner and typing HELP to discover what
    commands are available. Explore step by step!

    Returns:
        The secret string if found, None otherwise.
    """

    # STEP 1: Connect to the service
    # TODO: Use pwntools remote() to connect

    # STEP 2: Read the banner
    # TODO: Read until you see the prompt "MysteryNet> "

    # STEP 3: Send HELP to learn the commands
    # TODO: Read and print the response

    # STEP 4: Request a CHALLENGE
    # TODO: Read the response — it contains a Base64 string

    # STEP 5: Decode the challenge
    # TODO: Print both the encoded and decoded values

    # STEP 6: Send the answer
    # TODO: Read and verify the response says "Correct"

    # STEP 7: Request the SECRET
    # TODO: Read the response and extract the secret

    # STEP 8: Quit and Close

    pass  # Remove when you implement

# ─── Main ─────────────────────────────────────────────────────────────

def main():
    print("=" * 50)
    print("  Exercise 6: Custom Protocol Hacker")
    print("=" * 50)
    print()

    secret = interact_with_service(TARGET, PORT)

    if secret:
        print(f"\n🔑 Found: {secret.strip()}")
        print("   Save this! You'll need it for the Admin Gate.")
    else:
        print("\n⚠ Didn't find the secret.")
        print("  Try using r.interactive() to manually explore the protocol first!")
        print("  Then script the steps you discover.")

if __name__ == "__main__":
    main()
