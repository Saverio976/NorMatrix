#!/usr/bin/env python3
import sys

try:
    import regex
except ModuleNotFoundError:
    import sys
    import subprocess
    subprocess.run(["python3", "-m", "pip", "install", "regex"])
    p = subprocess.run([*sys.argv])
    exit(p.returncode)

try:
    from normatrix.source.main import main
except ModuleNotFoundError:
    from src.normatrix.source.main import main

exit(main())
