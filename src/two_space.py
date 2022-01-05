#!/usr/bin/env python3
import sys

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
    try:
        comment_index = line.index('//')
    except:
        comment_index = len(line)
    try:
        line.index('/*')
        IS_IN_COMMENT = True
    except:
        e = 0
        while e < len(line) and line[e] not in separator:
            e += 1
        try:
            if line[e:].index('  ') < comment_index:
                HAS_ERROR += 1
                print(f"{file}:{i + 1}:{line[:-1]}")
        except: pass

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
