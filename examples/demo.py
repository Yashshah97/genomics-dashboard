"""Demo for Genomics Tui Dashboard."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import genomics_dashboard

print("Genomics Tui Dashboard", "v" + genomics_dashboard.__version__)
print("modules:", [m for m in dir(genomics_dashboard) if not m.startswith('_')])
