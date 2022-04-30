try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
    from normatrix.source.custom_regex import re_sub
except ModuleNotFoundError:
    from src.normatrix.source.file_parser import CFileParse
    from src.normatrix.source.config import TypeLine
    from src.normatrix.source.custom_regex import re_sub

import re

def check(context, file: CFileParse) -> (int, int):
    nb_error = 0
    list_error = []

    if file.filepath.endswith("Makefile"):
        return (nb_error, 0, list_error)
    for i in range(len(file.sub_parsedline)):
        line = file.sub_parsedline[i]
        if line[0] == TypeLine.COMMENT:
            continue
        ll = re_sub(".*?\*\/", '', line[1], timeout=0.1)
        ll = re_sub("\/\*.*", '', ll, timeout=0.1)
        ll = re_sub("//.*", '', ll, timeout=0.1)
        nb = ll.count(';')
        if nb > 1 and 'for' not in ll:
            list_error.append(
                    (i + 1, f"only one statement per line ({ll})")
            )
            nb_error += 1
    return (nb_error, 0, list_error)
