try:
    from normatrix.source.config import TypeLine
    from normatrix.source.file_parser import CFileParse
except ModuleNotFoundError:
    from src.normatrix.source.config import TypeLine
    from src.normatrix.source.file_parser import CFileParse


def check(context, file: CFileParse) -> (int, int, list):
    nb_error = 0
    list_error = []
    nb_line = 0
    line_index_func = 0
    is_in_func = [False, False]

    if file.filepath.endswith("Makefile"):
        return (nb_error, 0, list_error)
    for i in range(len(file.sub_parsedline)):
        if not is_in_func[0] and file.sub_parsedline[i][0] == TypeLine.FUNCTION:
            is_in_func[0] = True
            line_index_func = i
        if is_in_func[1] and file.sub_parsedline[i][0] != TypeLine.FUNCTION:
            nb_line -= 1
            if nb_line > 20:
                nb_error += nb_line - 20
                list_error.append(
                    (line_index_func + 1, f"function number line ({nb_line} > 20)")
                )
            nb_line = 0
            is_in_func[0] = False
            is_in_func[1] = False
        if is_in_func[0] and file.sub_parsedline[i][1].startswith("{"):
            is_in_func[1] = True
        if is_in_func[1] and not file.sub_parsedline[i][1].startswith("}"):
            nb_line += 1
    return (nb_error, 0, list_error)
