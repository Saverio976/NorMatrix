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

    if file.filepath.endswith("Makefile"):
        return (nb_error, 1, list_error)
    for i in range(len(file.sub_parsedline)):
        line = file.sub_parsedline[i]
        if line[0] == TypeLine.COMMENT:
            continue
        ll = re.sub('\/\/.*', '', line[1])
        ll = re.sub("'(.)'", '', ll)
        m = re.search(",\S", ll)
        if m != None:
            list_error.append(
                    (i + 1, f"need a space after a comma ({ll[m.start():]})")
            )
            nb_error += 1
    return (nb_error, 1, list_error)
