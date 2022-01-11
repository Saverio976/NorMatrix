import re
from enum import Enum

class TypeLine(Enum):
    FUNCTION = 1
    MACRO = 2
    STRUCT = 3
    ENUM = 4
    GLOBAL = 5
    COMMENT = 6
    NONE = 7

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
    reg = [
        '^( ){0,}?\/\*(.*?\n{0,}){0,}\*\/',
        '^( ){0,}?\/\/.*',
        '\w{1,}(\*){0,} (\*){0,}\w{1,}\(((void)|(\n{0,1} *\w{1,}(\*){0,} (\*){0,}\w{1,}(\[[0-9]{0,}\]){0,}(, {0,1}\n{0,1} *\w{1,}(\*){0,} (\*){0,}\w{1,}(\[[0-9]{0,}\]){0,}){0,3})\n{0,1} {0,})\)\n{\n(.*\n)*?}',
        '^ {0,}#\w{1,}.*',
        '^(typedef ){0,1}(struct )(\w{1,} ){0,1}{\n {4}\w{1,} \w{1,};(\n {4}\w{1,} \w{1,};){0,}\n}( \w{1,}){0,1};',
        '^(typedef ){0,1}(enum )(\w{1,} ){0,1}{\n {4}\w{1,} \w{1,};(\n {4}\w{1,} \w{1,};){0,}\n}( \w{1,}){0,1};',
        '^(static ){0,1}(const ){0,1}\w{1,} \*{0,}\w{1,}(\[[0-9]{0,}\]){0,1} = ((\w{0,})|({\n{0,1} {0,}\w{0,}(,\n{0,1} {0,}\w{0,}){0,})|)\n{0,1}}{0,1};'
    ]
    status = [
        TypeLine.COMMENT,
        TypeLine.COMMENT,
        TypeLine.FUNCTION,
        TypeLine.MACRO,
        TypeLine.STRUCT,
        TypeLine.ENUM,
        TypeLine.GLOBAL
    ]
    for i, regex in enumerate(reg):
        res = re.search(regex, lines, re.MULTILINE)
        if res != None and res.start() <= len(lines.split('\n')[0]):
            return (status[i], lines[res.start():res.end()])
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
