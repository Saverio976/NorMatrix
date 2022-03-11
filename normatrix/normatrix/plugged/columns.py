try:
    from normatrix.source.file_parser import CFileParse
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse

def check(context, file: CFileParse) -> (int, int, list):
    nb_error = 0
    list_error = []
    for i in range(len(file.real_parsedline)):
        nb_cols = len(file.real_parsedline[i][1])
        if nb_cols > 80:
            list_error.append((i + 1, f"number of columns ({nb_cols} > 80)"))
            nb_error += 1
    return (nb_error, 0, list_error)
