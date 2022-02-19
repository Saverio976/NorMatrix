try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse
    from normatrix.normatrix.source.config import TypeLine

def check(context, file: CFileParse) -> (int, int):
    nb_error = 0
    for i in range(len(file.real_parsedline)):
        line = file.real_parsedline[i]
        if line[0] == TypeLine.COMMENT:
            continue
        nb_space = 0
        len_l = len(line[1])
        while len_l > 0 and nb_space < len_l and line[1][nb_space] == ' ':
            nb_space += 1
        if nb_space % 4 != 0:
            print(f"{file.basename}:{i + 1}: always four indent in source code")
            nb_error += 1
    return (nb_error, 1)
