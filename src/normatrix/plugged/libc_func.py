try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
    from normatrix.source.context import Context
    from normatrix.source.config import LIBC_BANNED_FUNC
    from normatrix.source.custom_regex import re_search, re_sub
except ModuleNotFoundError:
    from src.normatrix.source.file_parser import CFileParse
    from src.normatrix.source.config import TypeLine
    from src.normatrix.source.context import Context
    from src.normatrix.source.config import LIBC_BANNED_FUNC
    from src.normatrix.source.custom_regex import re_search, re_sub

import re

def check_libcfunc(context: Context, line: str) -> (bool, str):
    for elem in context.LIBC_BANNED_FUNC:
        m = re_search(f"\W{elem}\(", line, timeout=0.1)
        if m != None:
            return (True, elem)
    return (False, "")

def check(context: Context, file: CFileParse) -> (int, int, list):
    nb_error = 0
    list_error = []

    if file.filepath.endswith("Makefile"):
        return (nb_error, 0, list_error)
    for i in range(len(file.sub_parsedline)):
        line = file.sub_parsedline[i]
        if line[0] != TypeLine.COMMENT:
            ll = re_sub('\/\/.*', '', line[1], timeout=0.1)
            ok, func = check_libcfunc(context, ll)
            if ok:
                list_error.append((i + 1, f"no libc func ({func})"))
                nb_error += 1
    return (nb_error, 0, list_error)
