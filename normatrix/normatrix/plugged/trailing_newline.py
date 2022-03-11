try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse
    from normatrix.normatrix.source.config import TypeLine

def check(context, file: CFileParse) -> (int, int, list):
    nb_error = 0
    list_error = []
    last_is_no = False
    for i in range(len(file.sub_parsedline) - 1):
        if file.sub_parsedline[i][0] not in [TypeLine.COMMENT]:
            if last_is_no and file.sub_parsedline[i][1] == '':
                nb_error += 1
                list_error.append((i + 1, f"no 2 newline between functions"))
                last_is_no = False
            elif last_is_no == False and file.sub_parsedline[i][1] == '':
                last_is_no = True
            else:
                last_is_no = False
        else:
            last_is_no = False
    return (nb_error, 1, list_error)
