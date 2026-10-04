# Genomics Tui Dashboard

This is an interactive command-line interface for exploring and analyzing genomic data, featuring real-time updates and intuitive visualizations to help you navigate complex biological sequences with ease. Built from the ground up using pure Python, this project combines simplicity with robustness, making it easy to use and maintain. Whether you're a researcher or student, this tool is designed to streamline your workflow and accelerate your discoveries.

## What makes it unique

Combines DNA/RNA sequence analysis with a live-updating curses dashboard with panels and sparklines — a niche where few ready-made tools exist.

## Features

- **`genomics_dashboard/dashboard.py`** — Main application logic and curses setup
- **`genomics_dashboard/panels.py`** — Collection of panel classes for displaying data
- **`genomics_dashboard/sparklines.py`** — Implementation of sparkline display functionality
- **`genomics_dashboard/data_analysis.py`** — Functions for processing DNA/RNA sequence data
- **`genomics_dashboard/ui_helpers.py`** — Utility functions for curses UI manipulation
- **`genomics_dashboard/tests_test_core.py`** — Unit tests for core application logic

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/genomics-dashboard.git
cd genomics-dashboard

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
genomics-dashboard/
├── genomics_dashboard/
│   ├── dashboard.py
│   ├── panels.py
│   ├── sparklines.py
│   ├── data_analysis.py
│   ├── ui_helpers.py
│   ├── tests_test_core.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **genomics** · Archetype: **dashboard** ·
Built autonomously by JARVIS on 2026-10-03. MIT licensed.
