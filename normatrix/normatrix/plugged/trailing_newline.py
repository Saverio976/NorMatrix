try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse
    from normatrix.normatrix.source.config import TypeLine

def check(context, file: CFileParse) -> (int, int):
    nb_error = 0
    last_is_no = False
    for i in range(len(file.sub_parsedline) - 1):
        if file.sub_parsedline[i][0] not in [TypeLine.COMMENT]:
            if last_is_no and file.sub_parsedline[i][1] == '':
                nb_error += 1
                print(f"{file.basename}:{i + 1}: no 2 newline between functions")
                last_is_no = False
            elif last_is_no == False and file.sub_parsedline[i][1] == '':
                last_is_no = True
            else:
                last_is_no = False
        else:
            last_is_no = False
    if len(file.sub_parsedline) < 2:
        return (nb_error, 1)
    if file.real_parsedline[-1][1] == '' and file.real_parsedline[-2][1] == '':
        print(f"{file.basename}:{len(file.sub_parsedline) - 1}: extra new line at end of text")
        nb_error += 1
    return (nb_error, 1)
