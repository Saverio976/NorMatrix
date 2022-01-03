#!/usr/bin/env python3
import sys

HAS_ERROR = 0

TAB_NB = 0

file = sys.argv[1]
with open(file) as f: filelines: str = f.readlines()

for i in range(len(filelines)):
    line: str = filelines[i]
    if " ".join(line.split()).startswith("#if"):
        TAB_NB += 4
    elif " ".join(line.split()).startswith("#endif"):
        TAB_NB -= 4
    elif not line.startswith(" " * TAB_NB):
        print(f"{file}:{i}: {line[:-1]} (preprocessors directiv need 4 space after an #if)")
        HAS_ERROR += 1
    if TAB_NB < 0:
        print(f"{file}:{i}: {line[:-1]} (need an #if.. before an #endif)")
        HAS_ERROR += 1
exit(HAS_ERROR)
