try:
    from normatrix.source.config import TypeLine
    from normatrix.source.file_parser import CFileParse
except ModuleNotFoundError:
    from src.normatrix.source.config import TypeLine
    from src.normatrix.source.file_parser import CFileParse


def check(context, file: CFileParse) -> (int, int, list):
    nb_error = 0
    list_error = []
    last_is_no = False

    for i in range(len(file.real_parsedline) - 1):
        if file.real_parsedline[i][0] not in [TypeLine.COMMENT]:
            if last_is_no and file.real_parsedline[i][1] == "":
                nb_error += 1
                list_error.append((i + 1, "no 2 newline between functions"))
                last_is_no = False
            elif (last_is_no is False) and file.real_parsedline[i][1] == "":
                last_is_no = True
            else:
                last_is_no = False
        else:
            last_is_no = False
    return (nb_error, 1, list_error)
