try:
    from normatrix.source.config import TypeLine
    from normatrix.source.custom_regex import re_sub
    from normatrix.source.file_parser import CFileParse
except ModuleNotFoundError:
    from src.normatrix.source.config import TypeLine
    from src.normatrix.source.custom_regex import re_sub
    from src.normatrix.source.file_parser import CFileParse


def add_if_error(
    line: str, in_switch: bool, file: CFileParse, list_error: list, i: int
) -> bool:
    nb_error = 0

    if "switch " in line and line.endswith(" {"):
        in_switch = True
    if in_switch and line.endswith(" }"):
        in_switch = False
    condition = line.startswith(" " * 20 if in_switch else " " * 15)
    if condition:
        if line.startswith(" " * 16) and line.endswith(");"):
            return in_switch, nb_error
        if line.endswith(") {") or ") ? " in line:
            return in_switch, nb_error
        if i != 0 and file.real_parsedline[i - 1][1].endswith("\\"):
            return in_switch, nb_error
        if line.endswith(")") and (
            "if (" in file.sub_parsedline[i - 1][1]
            or "while (" in file.sub_parsedline[i - 1][1]
            or "for (" in file.sub_parsedline[i - 1][1]
        ):
            return in_switch, nb_error
        list_error.append((i + 1, f"maybe too many branch ? ({line})"))
        nb_error += 1
    return (in_switch, nb_error)


def check(context, file: CFileParse) -> (int, int, list):
    nb_error = 0
    in_switch = False
    is_in_func = [False, False]
    list_error = []

    if file.filepath.endswith("Makefile"):
        return (nb_error, 1, list_error)
    for i in range(len(file.sub_parsedline)):
        line = file.sub_parsedline[i][1]
        line = re_sub(r"\/\/.*", "", line, timeout=0.1)
        line = re_sub("^( )*$", "", line, timeout=0.1)
        if not is_in_func[0] and file.sub_parsedline[i][0] == TypeLine.FUNCTION:
            is_in_func[0] = True
        if is_in_func[1] and file.sub_parsedline[i][0] != TypeLine.FUNCTION:
            is_in_func[0] = False
            is_in_func[1] = False
        if is_in_func[0] and line.startswith("{"):
            is_in_func[1] = True
        if is_in_func[1] and not line.startswith("}"):
            in_switch, is_error = add_if_error(line, in_switch, file, list_error, i)
            nb_error += is_error
    return (nb_error, 1, list_error)
