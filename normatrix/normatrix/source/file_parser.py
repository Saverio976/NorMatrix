try:
    from normatrix.source.config import REG_TYPELINE
    from normatrix.source.config import TypeLine
except ModuleNotFoundError:
    from normatrix.normatrix.source.config import REG_TYPELINE
    from normatrix.normatrix.source.config import TypeLine

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
        lines = re.sub(r'".+?" ', '', lines)
        lines = re.sub(r'".+?"', '', lines)
        self.sub_filelines = lines.split('\n')

def get_status(lines: str) -> (TypeLine, str):
    for type_reg, regex_list in REG_TYPELINE.items():
        for regex in regex_list:
            res = regex.match(lines)
            if res != None and res.start() <= len(lines.split('\n')[0]):
                return (type_reg, lines[res.start():res.end()])
    return (TypeLine.NONE, lines.split('\n')[0])

def parse(filepath: str, dirname: str) -> CFileParse:
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
    return obj
