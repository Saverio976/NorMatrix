#!/usr/bin/env python3
from source.file_parser import CFileParse
from source.file_parser import TypeLine

def check(file: CFileParse) -> int:
    nb_error = 0
    nb_line = 0
    line_index_func = 0
    is_in_func = False
    for i in range(len(file.sub_parsedline)):
        if not is_in_func and file.sub_parsedline[i][0] == TypeLine.FUNCTION:
            is_in_func = True
            line_index_func = i
        if is_in_func and file.sub_parsedline[i][0] != TypeLine.FUNCTION:
            nb_line -= 1
            if nb_line > 20:
                nb_error += nb_line - 20
                print(f"{file.basename}:{line_index_func}: function number line ({nb_line} > 20)")
            nb_line = 0
            is_in_func = False
        if is_in_func and not (file.sub_parsedline[i][1].startswith('{') or \
                file.sub_parsedline[i][1].startswith('}')):
            nb_line += 1
    return nb_error
