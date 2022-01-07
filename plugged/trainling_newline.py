from source.file_parser import CFileParse
from source.file_parser import TypeLine
import re

def check(file: CFileParse) -> int:
    nb_error = 0
    last_is_no = False
    for i in range(len(file.sub_parsedline) - 1):
        if file.sub_parsedline[i][0] != TypeLine.COMMENT:
            if last_is_no and file.sub_parsedline[i][1] == '':
                nb_error += 1
                print(f"{file.basename}:{i + 1}: no 2 newline between functions")
                last_is_no = False
            elif last_is_no == False and file.sub_parsedline[i][1] == '':
                last_is_no = True
            else:
                last_is_no = False
    if file.sub_parsedline[-1][1] == '' and file.sub_parsedline[-2][1] == '':
        print(f"{file.basename}:{len(file.sub_parsedline) - 1}: extra new line at end of text")
        nb_error += 1
    return nb_error