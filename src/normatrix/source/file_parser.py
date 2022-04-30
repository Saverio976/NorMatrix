try:
    from normatrix.source.config import REG_TYPELINE
    from normatrix.source.config import TypeLine
    from normatrix.source.custom_regex import re_sub, re_search, re_match
except ModuleNotFoundError:
    from src.normatrix.source.config import REG_TYPELINE
    from src.normatrix.source.config import TypeLine
    from src.normatrix.source.custom_regex import re_sub, re_search, re_match

import re

class CFileParse:
    def __init__(self, filepath, name):
        """An object of a file 'parsed'."""
        # the relative path
        # : str
        self.basename = filepath[len(name) + 1:]
        # the absolute path
        # : str
        self.filepath = filepath
        # list of each line
        # : list[str]
        self.real_filelines = []
        # list of each line without str ("text here will be removed")
        # : list[str]
        self.sub_filelines = []
        # sub_filelines but with the type line
        # : list[tuple[TypeLine, str]]
        self.sub_parsedline = []
        # real_filelines but with the type line
        # : list[tuple[TypeLine, str]]
        self.real_parsedline = []

    def get_filelines(self):
        with open(self.filepath) as fd:
            lines = fd.read()
        self.real_filelines = lines.split('\n')
        m = re_search('"(.+?\\\n)+?(.+?)"', lines, timeout=0.1)
        while m != None:
            nb_nl = lines[m.start():m.end()].count("\n")
            replace = "\n" * nb_nl
            lines = re_sub('"(.+?\\\n)+?(.+?)"', f'"{replace}"', lines, count=1, timeout=0.1)
            m = re_search('"(.+?\\\n)+?(.+?)"', lines, timeout=1)
        m = re_search('"(.+?\\\n)+?(.+?)"', lines, timeout=1)
        lines = re_sub('".+?"', '""', lines)
        self.sub_filelines = lines.split('\n')

def get_status(lines: str) -> (TypeLine, str):
    for type_reg, regex_list in REG_TYPELINE.items():
        for regex in regex_list:
            res = re_match(lines, regex)
            if res != None and res.start() <= len(lines.split('\n')[0]):
                return (type_reg, lines[res.start():res.end()])
    return (TypeLine.NONE, lines.split('\n')[0])

def parse(filepath: str, dirname: str) -> (CFileParse, int):
    obj = CFileParse(filepath, dirname)
    obj.get_filelines()
    i = 0
    while i < len(obj.sub_filelines):
        rest = "\n".join(obj.sub_filelines[i:])
        (status, lines) = get_status(rest)
        for line in lines.split('\n'):
            obj.sub_parsedline.append((status, line))
            obj.real_parsedline.append((status, obj.real_filelines[i]))
            i += 1
    return (obj, len(obj.real_filelines))
