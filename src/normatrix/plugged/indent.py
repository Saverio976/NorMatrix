try:
    from normatrix.source.config import TypeLine
    from normatrix.source.file_parser import CFileParse
except ModuleNotFoundError:
    from src.normatrix.source.config import TypeLine
    from src.normatrix.source.file_parser import CFileParse


def check(context, file: CFileParse) -> (int, int, list):
    nb_error = 0
    list_error = []

    if file.filepath.endswith("Makefile"):
        return (nb_error, 0, list_error)
    for i in range(len(file.real_parsedline)):
        line = file.real_parsedline[i]
        if line[0] == TypeLine.COMMENT:
            continue
        nb_space = 0
        len_l = len(line[1])
        while len_l > 0 and nb_space < len_l and line[1][nb_space] == " ":
            nb_space += 1
        if nb_space % 4 != 0:
            list_error.append((i + 1, f"always four indent in source code ({line[1]})"))
            nb_error += 1
        if not (file.basename.endswith(".c") or file.basename.endswith(".h")):
            continue
        ll: str = line[1]
        if ll.strip().startswith("\t") or ll.strip().endswith("\t"):
            list_error.append((i + 1, "no \\t for indentation"))
            nb_error += 1
    return (nb_error, 1, list_error)
