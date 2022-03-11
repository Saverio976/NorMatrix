try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse
    from normatrix.normatrix.source.config import TypeLine

import re

def check(context, file: CFileParse) -> (int, int):
    nb_error = 0
    list_error = []
    for i in range(len(file.sub_parsedline)):
        line = file.sub_parsedline[i]
        if line[0] != TypeLine.COMMENT:
            ll = re.sub(".*?\*\/", '', line[1])
            ll = re.sub("\/\*.*", '', ll)
            ll = re.sub("//.*", '', ll)
            nb = ll.count(';')
            if nb > 1 and 'for' not in ll:
                list_error.append((i + 1, f"only one statement per line {ll}"))
                nb_error += 1
    return (nb_error, 0, list_error)
