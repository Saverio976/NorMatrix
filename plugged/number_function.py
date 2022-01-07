from source.file_parser import CFileParse
from source.file_parser import TypeLine

def check(file: CFileParse) -> int:
    number_func = 0
    last_is_in_func = False
    for line in file.sub_parsedline:
        if not last_is_in_func and line[0] == TypeLine.FUNCTION:
            last_is_in_func = True
        if last_is_in_func and line[0] != TypeLine.FUNCTION:
            number_func += 1
            last_is_in_func = False
    if number_func > 5:
        print(f"{file.basename}: only five function per file ({number_func} > 5)")
        return 1
    return 0
