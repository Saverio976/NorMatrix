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
        return (nb_error, 1, list_error)
    for i in range(len(file.real_parsedline)):
        line = file.real_parsedline[i]
        if line[0] != TypeLine.COMMENT:
            ll = line[1]
            if ll.split() != [] and ll.endswith("\t") or ll.endswith(" "):
                list_error.append((i + 1, "extra space at end of line"))
                nb_error += 1
            elif ll.split() == [] and (ll.startswith(" ") or ll.startswith("\t")):
                list_error.append((i + 1, "extra space at start of line"))
                nb_error += 1
    return (nb_error, 1, list_error)
