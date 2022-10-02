try:
    from normatrix.source.config import TypeLine, smart_match
    from normatrix.source.context import Context
    from normatrix.source.custom_regex import re_sub
    from normatrix.source.file_parser import CFileParse
except ModuleNotFoundError:
    from src.normatrix.source.config import TypeLine, smart_match
    from src.normatrix.source.context import Context
    from src.normatrix.source.custom_regex import re_sub
    from src.normatrix.source.file_parser import CFileParse


def get_escape_regex(s: str, need: bool) -> str:
    escape = ""
    for c in s:
        if c in "\\^$.|?*+()[]{}":
            escape += "\\"
        escape += c
    new = smart_match.get(escape, escape)
    if new != escape:
        return new
    if need:
        escape = f"[{escape}]"
    return escape


def check_regex_operator(
    l_nb: int, conf_op: list, line: str, list_error: list, preview: bool
) -> int:
    nb_error = 0
    new_line = line

    if len(conf_op) == 4:
        new_line = re_sub(conf_op[3], "", new_line, timeout=0.1)
    nb = 2 if preview else 1
    for _ in range(nb):
        rex = get_escape_regex(conf_op[0], True)
        new_line = re_sub(
            f"{rex}{get_escape_regex(conf_op[1], False)}", "", new_line, timeout=0.1
        )
        rex = get_escape_regex(conf_op[2], True)
        new_line = re_sub(
            f"{get_escape_regex(conf_op[1], False)}{rex}", "", new_line, timeout=0.1
        )
    if new_line.endswith(conf_op[1]):
        new_line = new_line[: -len(conf_op)]
    if conf_op[1] in new_line:
        list_error.append((l_nb, f"bad space for operator {conf_op[1]} ({new_line})"))
        nb_error += 1
    return nb_error


def check(context: Context, file: CFileParse) -> (int, int, list):
    nb_error = 0
    list_error = []

    if file.filepath.endswith("Makefile"):
        return (nb_error, 1, list_error)
    for i, line in enumerate(file.sub_parsedline):
        if line[0] == TypeLine.COMMENT:
            continue
        ll = re_sub("'.*?'", "", line[1], timeout=0.1)
        ll = re_sub(r"\/\/.*", "", ll, timeout=0.1)
        for conf in context.OPERATOR_LIST:
            nb_error += check_regex_operator(
                i + 1, conf, ll, list_error, context.ENABLE_PREVIEW
            )
    return (nb_error, 1, list_error)
