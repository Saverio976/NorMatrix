try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse
    from normatrix.normatrix.source.config import TypeLine

import re

reg = re.compile('^(\w{1,} ){1,}(\w){1,}\((.*?\n{0,1}){0,}?\) {0,1}\n{0,1}\{')

def get_only_func_decl(rest: str):
    res = reg.match(rest)
    if res != None and res.start() <= len(rest.split('\n')[0]):
        return rest[res.start():res.end()]
    return ''

def check(file: CFileParse) -> (int, int):
    nb_error = 0
    i = 0
    while i < len(file.sub_filelines):
        rest = "\n".join(file.sub_filelines[i:])
        lines = get_only_func_decl(rest)
        n = lines.count(',') + 1
        if n > 4:
            print(f"{file.basename}:{i + 1}: too many arguments ({n} > 4)")
            nb_error += 1
        for line in lines.split('\n'):
            i += 1
    return (nb_error, 0)
