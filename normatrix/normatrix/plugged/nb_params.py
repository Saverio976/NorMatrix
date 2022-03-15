try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse
    from normatrix.normatrix.source.config import TypeLine

import re

reg = re.compile('^(?!.*=)(\w{1,} {0,1}){2,}\((.*?\n{0,1}){0,}?\) {0,1}\n{0,1}\{')

def get_only_func_decl(rest: str):
    res = reg.match(rest)
    if res != None:
        only_decl = rest[res.start():res.end()]
        if "=" in only_decl or ";" in only_decl:
            return ''
        return only_decl
    return ''

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
        only_decl = re.sub("\(\*\w*?\)\((.|\n)*?\)", "", only_decl)
        n = only_decl.count(',') + 1
        if n > 4:
            list_error.append((i + 1, f"too many arguments ({n} > 4)"))
            nb_error += 1
    return (nb_error, 0, list_error)
