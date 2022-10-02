try:
    from normatrix.source.config import TypeLine
    from normatrix.source.file_parser import CFileParse
except ModuleNotFoundError:
    from src.normatrix.source.config import TypeLine
    from src.normatrix.source.file_parser import CFileParse


def check(context, file: CFileParse) -> (int, int, list):
    number_func = 0
    last_is_in_func = False

    if file.filepath.endswith("Makefile"):
        return (0, 0, [])
    for line in file.sub_parsedline:
        if not last_is_in_func and line[0] == TypeLine.FUNCTION:
            last_is_in_func = True
        if last_is_in_func and line[0] != TypeLine.FUNCTION:
            number_func += 1
            last_is_in_func = False
    if number_func > 5:
        return (1, 0, [(0, f"only five function per file ({number_func} > 5)")])
    return (0, 0, [])
