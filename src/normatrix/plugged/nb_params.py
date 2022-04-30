try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
    from normatrix.source.custom_regex import re_sub, re_match, re_compile
except ModuleNotFoundError:
    from src.normatrix.source.file_parser import CFileParse
    from src.normatrix.source.config import TypeLine
    from src.normatrix.source.custom_regex import re_sub, re_match, re_compile

reg = re_compile('^(?!.*=)(\w{1,} {0,1}){2,}\((.*?\n{0,1}){0,}?\) {0,1}\n{0,1}\{')
reg_func_name = re_compile('(?!.*=)(\w{1,} {0,1}){2,}')
alphabet = re_compile("[A-Z]")

def get_only_func_decl(rest: str):
    res = re_match(rest, reg, timeout=0.1)
    if res != None:
        only_decl = rest[res.start():res.end()]
        if "=" in only_decl or ";" in only_decl:
            return ''
        return only_decl
    return ''

def check_snake_case_function(only_decl: str, list_error: list, i: int) -> int:
    res = re_match(only_decl, reg_func_name, timeout=0.1)
    if res == None:
        return 0
    new = only_decl[res.start():res.end()]
    if len(new.split(' ')) < 2:
        return 0
    if re_match(new.split(' ')[1], alphabet) != None:
        list_error.append(
            (i + 1, f"function name is in snake case ({new.split(' ')[1]})")
        )
        return 1
    return 0

def check(context, file: CFileParse) -> (int, int, list):
    nb_error = 0
    list_error = []

    if file.basename.endswith('.h') or file.filepath.endswith("Makefile"):
        return (0, 0, [])
    for i, line in enumerate(file.sub_parsedline):
        if line[0] == TypeLine.COMMENT:
            continue
        all_lines = file.sub_parsedline[i:]
        rest_lines = "\n".join([x[1] for x in all_lines])
        only_decl = get_only_func_decl(rest_lines)
        nb_error += check_snake_case_function(only_decl, list_error, i)
        only_decl = re_sub("\((\*)+\w*?\)\((.|\n)*?\)", "", only_decl, timeout=0.1)
        if "()" in only_decl:
            list_error.append(
                (i + 1, "functions that takes no arguments should have void")
            )
            nb_error += 1
        n = only_decl.count(',') + 1
        if n > 4:
            list_error.append((i + 1, f"too many arguments ({n} > 4)"))
            nb_error += 1
    return (nb_error, 0, list_error)
