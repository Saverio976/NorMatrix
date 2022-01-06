#!/usr/bin/env python3
import sys
import re

HAS_ERROR = 0

IS_IN_COMMENT = False

file = sys.argv[1]
with open(file) as f: filelines: str = f.readlines()

def check_non_comment_line(line: str, i: int):
    global HAS_ERROR
    global IS_IN_COMMENT
    separator = [chr(k) for k in range(ord('a'), ord('z')+1)] + \
                [chr(k) for k in range(ord('A'), ord('Z')+1)] + \
                [chr(k) for k in range(ord('0'), ord('9')+1)]
    line: str = line.split("//")[0]
    line = line.split("/*")
    if len(line) == 1:
        line: str = line[0]
        e = 0
        while e < len(line) and line[e] not in separator:
            e += 1
        line: str = re.sub(r'".+?"', '', line[e:])
        try:
            line.index("  ")
            HAS_ERROR += 1
            print(f"{file}:{i + 1}:{line[:-1]}")
        except: pass
    else:
        IS_IN_COMMENT = True

for i in range(len(filelines)):
    line: str = filelines[i]
    if IS_IN_COMMENT:
        try:
            line.index('*/')
            IS_IN_COMMENT = False
        except: pass
    else:
        check_non_comment_line(line, i)

exit(HAS_ERROR)
