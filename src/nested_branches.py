#!/usr/bin/env python3
import sys

HAS_ERROR = 0
in_switch = False

file = sys.argv[1]
with open(file) as f: lines: list = f.readlines()

for i in range(len(lines)):
    line: str = lines[i]
    if "switch " in line and " {\n" in line:
        in_switch = True
    if in_switch and "}\n" in line:
        in_switch = False
    if in_switch: condition = line.startswith(" " * 20)
    else: condition = line.startswith(" " * 15)
    if condition:
        can_continue = (line.startswith(" " * 16) and line.endswith(");\n")) \
            or line.endswith(") {\n") or ") ? " in line \
            or ") ? " in lines[i - 1]
        if can_continue or (line.endswith(")\n") and (
                "if (" in lines[i - 1] or
                "while (" in lines[i - 1] or
                "for (" in lines[i - 1])):
            continue
        print(f"{file}:{i}: {line}", end='')
        HAS_ERROR += 1
exit(HAS_ERROR)
