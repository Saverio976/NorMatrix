try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
except ModuleNotFoundError:
    from src.normatrix.source.file_parser import CFileParse
    from src.normatrix.source.config import TypeLine

import re

def check(context, file: CFileParse) -> (int, int, list):
    nb_error = 0
    list_error = []

    if file.filepath.endswith("Makefile"):
        return (nb_error, 0, list_error)
    for i, line in enumerate(file.sub_parsedline):
        if line[0] == TypeLine.COMMENT and len(line[1]) >= 1:
            if line[1].startswith(' ') and line[1].strip(" ")[0] in ["*", "/"]:
                list_error.append(
                    (i + 1, f"need comments starts at first column of line")
                )
                nb_error += 1
        if line[0] != TypeLine.FUNCTION:
            continue
        if "//" in line[1] or "/*" in line[1]:
            list_error.append(
                (i + 1, f"no comments inside functions")
            )
            nb_error += 1
    return (nb_error, 1, list_error)
