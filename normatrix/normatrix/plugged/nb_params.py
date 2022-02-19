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
        return rest[res.start():res.end()]
    return ''

def check(context, file: CFileParse) -> (int, int):
    nb_error = 0
    if file.basename.endswith('.h'):
        return (0, 0)
    for i, line in enumerate(file.sub_parsedline):
        if line[0] == TypeLine.COMMENT:
            continue
        all_lines = file.sub_parsedline[i:]
        rest_lines = "\n".join([x[1] for x in all_lines])
        only_decl = get_only_func_decl(rest_lines)
        only_decl = re.sub("\(\*\w*?\)\((.|\n)*?\)", "", only_decl)
        n = only_decl.count(',') + 1
        if n > 4:
            print(f"{file.basename}:{i + 1}: too many arguments ({n} > 4)")
            nb_error += 1
    return (nb_error, 0)
