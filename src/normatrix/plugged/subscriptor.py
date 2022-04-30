try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
    from normatrix.source.custom_regex import re_search, re_sub
except ModuleNotFoundError:
    from src.normatrix.source.file_parser import CFileParse
    from src.normatrix.source.config import TypeLine
    from src.normatrix.source.custom_regex import re_search, re_sub

import re

def check(context, file: CFileParse) -> (int, int, list):
    nb_error = 0
    list_error = []

    if file.filepath.endswith("Makefile"):
        return (nb_error, 0, list_error)
    for i, line in enumerate(file.sub_parsedline):
        if line[0] == TypeLine.COMMENT:
            continue
        ll = re_sub(".*?\*\/", '', line[1], timeout=0.1)
        ll = re_sub("\/\*.*", '', ll, timeout=0.1)
        ll = re_sub("//.*", '', ll, timeout=0.1)
        m = re_search('(\[ )|( \])', ll, timeout=0.1)
        if m != None:
            list_error.append(
                    (i + 1, f"no space after [ or before ] ({line[1]})")
            )
            nb_error += 1
    return (nb_error, 0, list_error)
