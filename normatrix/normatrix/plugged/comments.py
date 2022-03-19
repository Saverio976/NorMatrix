try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse
    from normatrix.normatrix.source.config import TypeLine

import re

def check(context, file: CFileParse) -> (int, int, list):
    nb_error = 0
    list_error = []

    for i, line in enumerate(file.sub_parsedline):
        if line[0] != TypeLine.FUNCTION:
            continue
        if "//" in line[1] or "/*" in line[1]:
            list_error.append(
                    (i + 1, f"no comments inside functions")
            )
            nb_error += 1
    return (nb_error, 1, list_error)
