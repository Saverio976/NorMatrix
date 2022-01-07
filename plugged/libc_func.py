from source.file_parser import CFileParse
from source.file_parser import TypeLine
import re

def check_libcfunc(line: str) -> bool:
    s = ['printf', 'memset', 'stcpy', 'strcat']
    for elem in s:
        m = re.search(f"\W{elem}\(", line)
        if m != None:
            return True
    return False

def check(file: CFileParse) -> int:
    nb_error = 0
    for i in range(len(file.sub_parsedline)):
        line = file.sub_parsedline[i]
        if line[0] != TypeLine.COMMENT:
            if check_libcfunc(line[1]):
                print("{file.basename}:{i + 1}: no libc func")
                nb_error += 1
    return nb_error

