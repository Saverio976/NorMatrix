try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse
    from normatrix.normatrix.source.config import TypeLine

def print_error(line: int) -> (int, int, list):
    return (1, 0, [(line, "bad header")])

def check(context, file: CFileParse) -> (int, int, list):
    lines = file.real_filelines[:]
    if len(lines) < 6:
        return print_error(0)
    if lines[0] != "/*":
        return print_error(1)
    if not lines[1].startswith("** EPITECH PROJECT, "):
        return print_error(2)
    if len(lines[2]) < 4 or not lines[2].startswith("** "):
        return print_error(3)
    if lines[3] != "** File description:":
        return print_error(4)
    i = 4
    while i < len(lines) and lines[i] != "*/":
        if len(lines[i]) < 4 or not lines[i].startswith("** "):
            return print_error(i + 1)
        i += 1
    if i >= len(lines):
        return print_error(i + 1)
    if lines[i] != "*/":
        return print_error(i + 1)
    return (0, 0, [])
