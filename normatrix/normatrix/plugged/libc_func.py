try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.file_parser import TypeLine
    from normatrix.source.config import LIBC_BANNED_FUNC
except:
    from normatrix.normatrix.source.file_parser import CFileParse
    from normatrix.normatrix.source.file_parser import TypeLine
    from normatrix.normatrix.source.config import LIBC_BANNED_FUNC

import re

def check_libcfunc(line: str) -> (bool, str):
    for elem in LIBC_BANNED_FUNC:
        m = re.search(f"\W{elem}\(", line)
        if m != None:
            return (True, elem)
    return (False, "")

def check(file: CFileParse) -> (int, int):
    nb_error = 0
    for i in range(len(file.sub_parsedline)):
        line = file.sub_parsedline[i]
        if line[0] != TypeLine.COMMENT:
            ll = re.sub('\/\/.*', '', line[1])
            ok, func = check_libcfunc(ll)
            if ok:
                print(f"{file.basename}:{i + 1}: no libc func ({func})")
                nb_error += 1
    return (nb_error, 0)