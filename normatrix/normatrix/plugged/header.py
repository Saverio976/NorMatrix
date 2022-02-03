try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse
    from normatrix.normatrix.source.config import TypeLine

def print_error(file: str) -> (int, int):
    print(f"{file}: bad header")
    return (1, 0)

def check(file: CFileParse) -> (int, int):
    nb_error = 0
    lines = file.real_filelines[:6]
    if len(lines) != 6:
        return print_error(file.basename)
    if lines[0] != "/*":
        return print_error(file.basename)
    if not lines[1].startswith("** EPITECH PROJECT, "):
        return print_error(file.basename)
    if len(lines[2]) < 4 or not lines[2].startswith("** "):
        return print_error(file.basename)
    if lines[3] != "** File description:":
        return print_error(file.basename)
    if len(lines[4]) < 4 or not lines[4].startswith("** "):
        return print_error(file.basename)
    if lines[5] != "*/":
        return print_error(file.basename)
    return (0, 0)
