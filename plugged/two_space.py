#!/usr/bin/env python3
from source.file_parser import CFileParse
from source.file_parser import TypeLine
import re

def check_non_comment_line(file: CFileParse, line: str, i: int, IS_IN_COMMENT: bool, nb_error: int):
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
        try:
            line[e:].index("  ")
            nb_error += 1
            print(f"{file.basename}:{i + 1}: two space alone ({line[e:]})")
        except: pass
    else:
        IS_IN_COMMENT = True
    return (IS_IN_COMMENT, nb_error)

def check(file: CFileParse) -> int:
    IS_IN_COMMENT = False
    nb_error = 0
    filelines = file.sub_filelines
    for i in range(len(filelines)):
        line: str = filelines[i]
        if IS_IN_COMMENT:
            try:
                line.index('*/')
                IS_IN_COMMENT = False
            except: pass
        else:
            IS_IN_COMMENT, nb_error = check_non_comment_line(file, line, i, IS_IN_COMMENT, nb_error)
    return nb_error