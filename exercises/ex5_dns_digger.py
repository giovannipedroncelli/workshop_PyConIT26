#!/usr/bin/env python3
"""
Exercise 5 — DNS Digger
========================

OBJECTIVE:
    Query the DNS service to discover hidden records and extract SECRET_3.

WHAT YOU'LL LEARN:
    - How DNS works (queries, record types: A, TXT, MX, etc.)
    - Using dnspython to make custom DNS queries
    - Why DNS can hold secrets (TXT records are commonly used for verification)

BACKSTORY:
    From Exercise 1 you found a UDP-based service on one of the ports.
    If it looks like DNS, we can query it directly!

    DNS isn't just about resolving domain names — TXT records can store
    arbitrary text, and organizations often hide configuration data there.

INSTRUCTIONS:
    Fill in the TODO sections, then run:
        python ex5_dns_digger.py
"""

import dns.resolver
import dns.message
import dns.query
import re

# ─── Configuration ────────────────────────────────────────────────────

TARGET = "127.0.0.1"
DNS_PORT = None  # TODO: Fill in the DNS port you discovered
START_DOMAIN = None # TODO: Fill in the domain from the previous exercise

def query_dns(server: str, port: int, domain: str, rdtype: str) -> list[str]:
    """
    Send a DNS query to a specific server and return the answers.

    Args:
        server: DNS server IP
        port:   DNS server port
        domain: Domain name to query
        rdtype: Record type ("A", "TXT", "MX", etc.)

    Returns:
        List of answer strings
    """

    # Note: We can't use the system resolver because our DNS server
    # runs on a non-standard port. We need to send the query
    # directly using dns.message and dns.query.
    try:
        q = dns.message.make_query(domain, rdtype)
        response = dns.query.udp(q, server, port=port, timeout=5)
        answers = []
        for rrset in response.answer:
            for rdata in rrset:
                answers.append(str(rdata).strip('"'))
        return answers
    except Exception as e:
        print(f"  Error querying {domain}/{rdtype}: {e}")
        return []

def extract_next_domain(text: str) -> str | None:
    """Extract NEXT=domain from a TXT answer."""
    m = re.search(r"NEXT=([a-zA-Z0-9.-]+)", text)
    if m:
        return m.group(1).strip().lower()
    return None

# ─── Main ─────────────────────────────────────────────────────────────

def main():
    print("=" * 50)
    print("  Exercise 5: DNS Digger")
    print("=" * 50)
    print()

    print(f"Start domain (from previous hint): {START_DOMAIN}")
    print()

    current_domain = START_DOMAIN
    visited = set()
    secret = None

    # Follow the TXT trail: NEXT=... until you find SECRET_3.
    while current_domain and current_domain not in visited and not secret:
        visited.add(current_domain)
        print(f"[+] Querying {current_domain}")

        # TODO: Query A record for current_domain and print it if present

        # TODO: Query TXT record for current_domain and print it
        txt_results = []

        next_domain = None
        # TODO: For each TXT answer:
        #   - if it contains "SECRET", save it to secret
        #   - if it contains NEXT=..., set next_domain using extract_next_domain

        current_domain = next_domain
        print()

    print(f"Discovered domains: {', '.join(sorted(visited))}")

    if secret:
        print(f"🔑 Found: {secret.strip()}")
        print("   Save this! You'll need it for the Admin Gate.")
    else:
        print("⚠ No secret found. Check your DNS query implementation.")
        print("  Make sure you're querying TXT records, not just A records!")

if __name__ == "__main__":
    main()
