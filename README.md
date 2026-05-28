# Participants Repository - The Art of Exploration

This repository is the **participants-only kit** for the PyCon Italia 2026 workshop.

It intentionally contains only:
- `mystery_machine.py`
- `requirements.txt`
- unsolved files in `exercises/`

It intentionally does **not** contain any solutions.

# The Art of Exploration: Build Your Own Network Scanner with Python

## PyCon Italia 2026 — 120-Minute Workshop

> Stop using tools, start building them. In this workshop, we turn Python into a network radar.

---

## What You'll Learn

1. **Build a TCP Port Scanner** from scratch using raw sockets
2. **Banner Grabbing** — identify services by their responses
3. **Protocol Interaction** — speak FTP, HTTP, DNS, and custom protocols
4. **pwntools** — the Swiss Army knife for network interaction
5. **Chain it all together** — solve a multi-stage challenge

---

## Prerequisites

- Python 3.10+ installed
- Basic Python knowledge (functions, loops, strings)
- A terminal / command line
- No prior security experience needed!

---

## Quick Setup

### 1. Create a virtual environment

```bash
cd participant-kit
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\Activate.ps1  # Windows PowerShell
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the Mystery Machine (the target)

**Option B — Local Python (recommended):**
```bash
python mystery_machine.py
```

### 4. Verify everything works

```bash
cd exercises
python ex0_setup_check.py
```

You should see: `All systems go! The Mystery Machine is running.`

---

## Workshop Schedule (120 min)

| Time        | Exercise | Topic                                  |
|-------------|----------|----------------------------------------|
| 0:00–0:10   | —        | Introduction & Setup                   |
| 0:10–0:25   | Ex 1     | Build a TCP Port Scanner               |
| 0:25–0:40   | Ex 2     | Banner Grabbing & Service Fingerprint  |
| 0:40–0:55   | Ex 3     | FTP Explorer                           |
| 0:55–1:05   | —        | Break                                  |
| 1:05–1:20   | Ex 4     | HTTP Detective                         |
| 1:20–1:30   | Ex 5     | DNS Digger                             |
| 1:30–1:45   | Ex 6     | Custom Protocol Hacker (intro pwntools)|
| 1:45–1:55   | Ex 7     | Admin Gate — Final Challenge           |
| 1:55–2:00   | —        | Wrap-up & Bonus (Ex 8)                 |

---

## Files

```
participant-kit/
├── README.md               ← You are here
├── requirements.txt        ← Python dependencies
├── mystery_machine.py      ← Local Python target launcher
└── exercises/              ← YOUR FILES (fill in the TODOs!)
    ├── ex0_setup_check.py
    ├── ex1_port_scanner.py
    ├── ex2_banner_grabber.py
    ├── ex3_ftp_explorer.py
    ├── ex4_http_detective.py
    ├── ex5_dns_digger.py
    ├── ex6_protocol_hacker.py
    ├── ex7_admin_gate.py
    └── ex8_full_autopwn.py  ← Bonus
```

> **No solutions folder** — the point is to discover and build everything yourself!
> If you get stuck, ask the instructor for hints.
