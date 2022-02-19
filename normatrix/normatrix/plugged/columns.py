try:
    from normatrix.source.file_parser import CFileParse
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse

def check(context, file: CFileParse) -> (int, int):
    nb_error = 0
    for i in range(len(file.real_parsedline)):
        nb_cols = len(file.real_parsedline[i][1])
        if nb_cols > 80:
            print(f"{file.basename}:{i + 1}: number columns ({nb_cols} > 80)")
            nb_error += 1
    return (nb_error, 0)
