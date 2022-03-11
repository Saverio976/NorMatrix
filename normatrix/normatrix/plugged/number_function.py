try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse
    from normatrix.normatrix.source.config import TypeLine

def check(context, file: CFileParse) -> (int, int, list):
    number_func = 0
    last_is_in_func = False
    for line in file.sub_parsedline:
        if not last_is_in_func and line[0] == TypeLine.FUNCTION:
            last_is_in_func = True
        if last_is_in_func and line[0] != TypeLine.FUNCTION:
            number_func += 1
            last_is_in_func = False
    if number_func > 5:
        return (1, 0, [(0, f"only five function per file ({number_func} > 5)")])
    return (0, 0, [])
