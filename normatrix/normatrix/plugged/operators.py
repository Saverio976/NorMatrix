try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
    from normatrix.source.context import Context
    from normatrix.source.config import smart_match
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse
    from normatrix.normatrix.source.config import TypeLine
    from normatrix.normatrix.source.context import Context
    from normatrix.normatrix.source.config import smart_match

import re

def get_escape_regex(s: str, need: bool) -> str:
    l = ""
    for c in s:
        if c in "\\^$.|?*+()[]{}":
            l += "\\"
        l += c
    new = smart_match.get(l, l)
    if new != l:
        return new
    if need:
        l = f'[{l}]'
    return l

def check_regex_operator(filename: str, l_nb: int, conf_op: list, line: str, list_error: list) -> int:
    nb_error = 0
    new_line = line
    if len(conf_op) == 4:
        new_line = re.sub(conf_op[3], '', new_line)
    rex = get_escape_regex(conf_op[0], True)
    new_line = re.sub(f"{rex}{get_escape_regex(conf_op[1], False)}", '', new_line)
    rex = get_escape_regex(conf_op[2], True)
    new_line = re.sub(f"{get_escape_regex(conf_op[1], False)}{rex}", '', new_line)
    if (new_line.endswith(conf_op[1])):
        new_line = new_line[:-len(conf_op)]
    try:
        new_line.index(conf_op[1])
        list_error.append((l_nb, f"bad space for operator: {conf_op[1]}"))
        nb_error += 1
    except ValueError: pass
    return nb_error

def check(context: Context, file: CFileParse) -> (int, int, list):
    nb_error = 0
    list_error = []
    for i, line in enumerate(file.sub_parsedline):
        if line[0] == TypeLine.COMMENT:
            continue
        ll = re.sub("'.*?'", '', line[1])
        ll = re.sub("\/\/.*", '', ll)
        for conf in context.OPERATOR_LIST:
            nb_error += check_regex_operator(file.basename, i + 1, conf, ll, list_error)
    return (nb_error, 1, list_error)
