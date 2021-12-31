#!/usr/bin/env python3
import sys

HAS_ERROR = 0

file = sys.argv[1]
with open(file) as f: lines: list = f.readlines()

for i in range(len(lines)):
    line: str = lines[i]
    if line.startswith(" " * 15):
        can_continue = line.endswith(");\n") or line.endswith(") {\n")
        if can_continue or (line.endswith(")\n") and (
                "if (" in lines[i - 1] or
                "while (" in lines[i - 1] or
                "for (" in lines[i - 1])):
            continue
        print(f"{file}:{i}: {line}", end='')
        HAS_ERROR = 1
exit(HAS_ERROR)
