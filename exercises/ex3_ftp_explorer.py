#!/usr/bin/env python3
"""
Exercise 3 — FTP Explorer
==========================

OBJECTIVE:
    Connect to the FTP service, explore the file system, and find SECRET_1.

WHAT YOU'LL LEARN:
    - Python's built-in `ftplib` for FTP protocol interaction
    - FTP control channel vs data channel (two TCP connections)
    - Directory listing and file navigation
    - Metadata-driven hunting with NLST, SIZE, and MDTM

BACKSTORY:
    From Exercise 2, you identified an FTP server on one of the open ports.
    What did the banner say about login? Let's explore what's inside!

INSTRUCTIONS:
    Fill in the TODO sections, then run:
        python ex3_ftp_explorer.py
"""

from ftplib import FTP
from io import BytesIO

# ─── Configuration ────────────────────────────────────────────────────

TARGET = "127.0.0.1"
FTP_PORT = None  # TODO: Fill in the FTP port you discovered in Exercise 2

def explore_ftp(host: str, port: int) -> str | None:
    """
    Connect to the FTP server, explore the filesystem, and find the secret.

    Returns:
        The secret string if found, None otherwise.
    """

    # STEP 1: Connect and login anonymously
    # NOTE: FTP uses two TCP channels.
    #   - Control channel: commands/replies on the server port (2121 in this lab)
    #   - Data channel: opened per transfer in passive mode (server high ports)
    # TODO: Create an FTP object and connect to host:port
    # TODO: Login with anonymous credentials (user="anonymous", passwd="")
    # OPTIONAL DEBUG: ftp.set_debuglevel(2) to see PASV/control messages

    # STEP 2: List the root directory
    # TODO: Use ftp.retrlines("LIST") or ftp.nlst() to see what files are available
    # TODO: Print the listing to see what's there

    # STEP 3: Read welcome.txt
    # TODO: Download and print the content of welcome.txt
    #       where callback writes to a BytesIO buffer

    # STEP 4: Follow the hint and enter archive/
    # TODO: Use ftp.cwd("archive") and list files.

    # STEP 5: Hunt SECRET_1 using metadata (not brute-force reading all files)
    # NOTE: some FTP servers require binary mode for SIZE
    # TODO: Run ftp.voidcmd("TYPE I") right before each ftp.size(...)
    # TODO: Use ftp.nlst() to collect filenames.
    # TODO: Filter candidate files (audit_*).
    # TODO: Use ftp.size(name) and ftp.sendcmd(f"MDTM {name}") to rank candidates.
    # TODO: Download only the best candidate with retrbinary().

    # STEP 6: Close the connection
    # TODO: ftp.quit()

    pass  # Remove when you implement

# ─── Main ─────────────────────────────────────────────────────────────

def main():
    print("=" * 50)
    print("  Exercise 3: FTP Explorer")
    print("=" * 50)
    print()

    secret = explore_ftp(TARGET, FTP_PORT)

    if secret:
        print(f"\n🔑 Found: {secret.strip()}")
        print("   Save this! You'll need it for the Admin Gate.")
    else:
        print("\n⚠ No secret found. Check your implementation.")
    print("  Hint: Use welcome.txt + metadata (SIZE/MDTM), not brute-force RETR on every file.")

if __name__ == "__main__":
    main()
