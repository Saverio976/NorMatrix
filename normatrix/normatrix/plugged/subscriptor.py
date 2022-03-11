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
        if line[0] != TypeLine.COMMENT:
            ll = re.sub(".*?\*\/", '', line[1])
            ll = re.sub("\/\*.*", '', ll)
            ll = re.sub("//.*", '', ll)
            m = re.search('(\[ )|( \])', ll)
            if m != None:
                list_error.append((i + 1, f"no space after [ or before ] ({line[1]})"))
                nb_error += 1
    return (nb_error, 0, list_error)
