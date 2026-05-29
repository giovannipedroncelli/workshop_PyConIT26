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
FTP_PORT = 2121  # TODO: Fill in the FTP port you discovered in Exercise 2

def explore_ftp(host: str, port: int) -> str | None:
    """
    Connect to the FTP server, explore the filesystem, and find the secret.

    Returns:
        The secret string if found, None otherwise.
    """

    ftp = FTP()
    ftp.connect(host,port)
    print(ftp.getwelcome())
    print(ftp.login(user='anonymous',passwd=""))
    
    print("File list")
    ftp.retrlines("LIST")

    buf = BytesIO()
    ftp.retrbinary("RETR welcome.txt", buf.write)
    print(buf.getvalue().decode())

    ftp.cwd("archive")
    ftp.retrlines("LIST")

    candidates = []
    for name in ftp.nlst():
        if not name.lower().startswith("audit_"):
            continue
        ftp.voidcmd("TYPE I")
        size = ftp.size(name)
        mdtm = ftp.sendcmd(f"MDTM {name}")
        print(mdtm)

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
    print("  Hint: Use welcome.txt + metadata (SIZE/MDTM). Evaluate newest by MDTM, then apply the <80 bytes filter.")

if __name__ == "__main__":
    main()
