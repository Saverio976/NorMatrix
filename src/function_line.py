#!/usr/bin/env python3
import sys

HAS_ERROR = 0

file = sys.argv[1]
with open(file) as f: filelines: str = f.read()

try:
    match_start = filelines.index('\n{')
except:
    match_start = 0

while match_start != 0:
    match_end = filelines.index('\n}', match_start)
    tmp_str: str = filelines[match_start:match_end]
    number_line = tmp_str.count('\n') - 1
    if number_line > 20:
        HAS_ERROR = 1
        line_index = filelines.index(tmp_str)
        line_n = filelines.count('\n', 0, match_start)
        print(
            f"{file}:{line_n}: number line per function ({number_line} > 20)"
        )
    try:
        match_start = filelines.index('\n{', match_end)
    except:
        match_start = 0
exit(HAS_ERROR)
