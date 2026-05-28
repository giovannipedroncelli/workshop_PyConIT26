#!/usr/bin/env python3
"""
Exercise 1 — Build a TCP/UDP Port Scanner
======================================

OBJECTIVE:
    Scan the Mystery Machine (127.0.0.1) to discover which TCP and UDP ports are open.
    We know the services are running on ports between 1 and 10000.

WHAT YOU'LL LEARN:
    - How TCP connections work (the 3-way handshake)
    - Why UDP scanning behaves differently from TCP
    - Using Python's `socket` module for network programming
    - Connect scanning: the simplest and most reliable scan technique

INSTRUCTIONS:
    Fill in the TODO sections below, then run:
        python ex1_port_scanner.py

OPTIONAL EXTRA (NOT PART OF THE WORKSHOP EXERCISE):
    You can also try a deeper scan mode just out of curiosity:
        python ex1_port_scanner.py --mode deep

EXPECTED OUTPUT:
    You should discover several open TCP ports on the Mystery Machine.
    For UDP, treat "open|filtered" as ambiguous (normal behavior):
    only a real UDP reply confirms "open".
"""

import argparse
import socket
import time
from concurrent.futures import ThreadPoolExecutor

# ─── Configuration ────────────────────────────────────────────────────
TARGET = "127.0.0.1"
WORKSHOP_PORT_RANGE = range(1, 10001)
WORKSHOP_TCP_TIMEOUT = 0.05
WORKSHOP_TCP_MAX_WORKERS = 200
WORKSHOP_UDP_TIMEOUT = 0.12
WORKSHOP_UDP_MAX_WORKERS = 300

# Optional curiosity mode: wider scan with more conservative timing.
DEEP_PORT_RANGE = range(1, 65536)
DEEP_TCP_TIMEOUT = 0.1
DEEP_TCP_MAX_WORKERS = 300
DEEP_UDP_TIMEOUT = 0.2
DEEP_UDP_MAX_WORKERS = 400

def scan_tcp_port(host: str, port: int, timeout: float) -> bool:
    """
    Attempt a TCP connection to host:port.

    Returns True if the port is open, False otherwise.

    A TCP "connect scan" works by completing the 3-way handshake:
        1. We send SYN
        2. If the port is open, the server replies SYN-ACK
        3. We complete with ACK → connection established!
    If the port is closed, we get a RST (connection refused).

    Python's socket.connect() does all of this for us.
    """

    # TODO: Create a TCP socket (AF_INET, SOCK_STREAM)
    # TODO: Set the timeout so we don't wait forever
    # TODO: Try to connect to (host, port)
    # TODO: If connect succeeds → return True
    # TODO: If we get a timeout or connection refused → return False
    # TODO: Make sure to close the socket!

    pass  # Remove this line when you implement the function

def scan_udp_port(host: str, port: int, timeout: float) -> str:
    """
    Probe a UDP port and classify it as:
        - "open"          (we got a UDP reply)
        - "closed"        (ICMP unreachable / OS error)
        - "open|filtered" (no reply within timeout)

    Why not just connect_ex like TCP?
        UDP has no handshake, so "connected" does not prove the service is open.
    """

    # TODO: Create a UDP socket (AF_INET, SOCK_DGRAM)
    # TODO: Set timeout
    # TODO: Connect to (host, port)
    # TODO: Send a generic probe payload (e.g. b"scan")
    # TODO: Try recv(...)
    #       - if data arrives: return "open"
    #       - if timeout: return "open|filtered"
    # TODO: Handle Windows/Linux closed-port errors too
    #       (examples: 111, 61, 10054, 10061) -> "closed"

    pass  # Remove this line when you implement the function

def scan_range(
    host: str,
    ports,
    protocol: str,
    timeout: float,
    max_workers: int,
) -> tuple[list[int], list[int]]:
    """
    Scan a range of ports and return a list of open ones.

    Args:
        host:    Target IP address
        ports:   Iterable of port numbers to scan
        timeout: Connection timeout in seconds

    Returns:
        (open_ports, open_or_filtered_ports)
        For TCP, open_or_filtered_ports will be empty.
    """
    open_ports = []
    open_or_filtered_ports = []

    print(
        f"Scanning {protocol.upper()} on {host} — ports {ports.start}-{ports.stop - 1} "
        f"({max_workers} workers)..."
    )
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        if protocol == "tcp":
            results = executor.map(lambda p: (p, scan_tcp_port(host, p, timeout)), ports)
            for port, is_open in results:
                if is_open:
                    open_ports.append(port)
                    print(f"  [OPEN] TCP {port}")
        else:
            results = executor.map(lambda p: (p, scan_udp_port(host, p, timeout)), ports)
            for port, state in results:
                if state == "open":
                    open_ports.append(port)
                    print(f"  [OPEN] UDP {port}")
                elif state == "open|filtered":
                    open_or_filtered_ports.append(port)

    elapsed = time.time() - start_time
    print(f"\nScan complete in {elapsed:.1f}s")
    return sorted(open_ports), sorted(open_or_filtered_ports)

# ─── Main ─────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Exercise 1 port scanner")
    parser.add_argument(
        "--mode",
        choices=("workshop", "deep"),
        default="workshop",
        help="workshop=default fast scan for class, deep=optional curiosity scan",
    )
    parser.add_argument(
        "--protocol",
        choices=("tcp", "udp", "both"),
        default="both",
        help="tcp=only TCP, udp=only UDP, both=run both scans",
    )
    parser.add_argument(
        "--show-udp-ambiguous",
        action="store_true",
        help="print UDP open|filtered ports (usually noisy on localhost)",
    )
    return parser.parse_args()

def main():
    args = parse_args()

    if args.mode == "deep":
        selected_range = DEEP_PORT_RANGE
        tcp_timeout = DEEP_TCP_TIMEOUT
        tcp_workers = DEEP_TCP_MAX_WORKERS
        udp_timeout = DEEP_UDP_TIMEOUT
        udp_workers = DEEP_UDP_MAX_WORKERS
        mode_label = "deep (optional curiosity mode)"
    else:
        selected_range = WORKSHOP_PORT_RANGE
        tcp_timeout = WORKSHOP_TCP_TIMEOUT
        tcp_workers = WORKSHOP_TCP_MAX_WORKERS
        udp_timeout = WORKSHOP_UDP_TIMEOUT
        udp_workers = WORKSHOP_UDP_MAX_WORKERS
        mode_label = "workshop (default)"

    print("=" * 50)
    print("  Exercise 1: TCP/UDP Port Scanner")
    print("=" * 50)
    print(f"  Mode: {mode_label}")
    print(f"  Protocol: {args.protocol}")
    print()

    if args.protocol in ("tcp", "both"):
        tcp_open, _ = scan_range(
            TARGET,
            selected_range,
            protocol="tcp",
            timeout=tcp_timeout,
            max_workers=tcp_workers,
        )

        print(f"\nResults: {len(tcp_open)} open TCP port(s) found on {TARGET}")
        for port in tcp_open:
            print(f"  → TCP {port} is OPEN")

        if not tcp_open:
            print("  No open TCP ports found! Make sure the Mystery Machine is running.")
            print("  See: python ex0_setup_check.py")

    if args.protocol in ("udp", "both"):
        udp_open, udp_open_or_filtered = scan_range(
            TARGET,
            selected_range,
            protocol="udp",
            timeout=udp_timeout,
            max_workers=udp_workers,
        )

        print(f"\nResults: {len(udp_open)} open UDP port(s) found on {TARGET}")
        for port in udp_open:
            print(f"  → UDP {port} is OPEN")

        if udp_open_or_filtered:
            if args.show_udp_ambiguous:
                print(
                    f"  Note: {len(udp_open_or_filtered)} UDP port(s) are open|filtered "
                    "(no response to probe)."
                )
                preview = udp_open_or_filtered[:20]
                print(f"  open|filtered sample: {preview}")
            else:
                print(
                    f"  Note: {len(udp_open_or_filtered)} UDP port(s) are ambiguous "
                    "(open|filtered) and hidden by default."
                )
                print("  Use --show-udp-ambiguous to print them.")

    print("\nSave these ports — you'll need them in Exercise 2.")

if __name__ == "__main__":
    main()
