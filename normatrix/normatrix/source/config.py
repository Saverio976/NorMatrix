import re
from enum import Enum

LIBC_BANNED_FUNC = [
        'printf',
        'memset',
        'strcpy',
        'strcat',
        'calloc'
]

BAD_FILE_EXTENSION = [
        '.a',
        '.o',
        '.so',
        '.gch',
        '~',
        '#',
        '.d'
]

smart_match = {
        ':ALL:': '.',
        ':NOTHING:': '{0}',
        ':ALPHANUM:': '[0-9a-zA-Z]',
        ':NUM:': '[0-9]',
        ':ALPHA:': '[a-zA-Z]',
        ':NOSPACE:': '\S'
}

OPERATOR_LIST = [
        (' ([+',    '+',    '+])= ',        '(\+\+\w)|(\w\+\+)'),
        (' ([-{',    '-',    '-])=> ',      '(--\w)|(\w--)'),
        (' ([/*',   '*',    ':NOTHING:',    '[\[\{\( ]\*{2,}'),
        (' (/*',    '/',    '*/= ',         '(<.*?\/.*?\.h>)|(".*?\/.*?\.h")'),
        ('< ',      '<',    ':ALL:'),
        (':ALL:',   '>',    ' >='),
        (' ',       '&',    ':ALL:'),
        ('([ ',     '!',    ':ALL:'),
        ('/+*-=! ', '=',    '= '),
        (':ALL:',   '(',    ':ALL:'),
        (':ALL:',   ')',    '}]) ;')
]

class TypeLine(Enum):
    FUNCTION = 1
    MACRO = 2
    STRUCT = 3
    ENUM = 4
    GLOBAL = 5
    COMMENT = 6
    NONE = 7
    FUNC_PROTO = 8

REG_TYPELINE = {
    TypeLine.COMMENT: [
        re.compile("^( ){0,}?\/\*(.*?\n{0,}){0,}\*\/"),
        re.compile("^( ){0,}?\/\/.*")
    ],
    TypeLine.MACRO: [
        re.compile("^ {0,}#\w{1,}.*")
    ],
    TypeLine.STRUCT: [
        re.compile("^(typedef ){0,1}(struct )(\w{1,} ){0,1}{\n {4}\w{1,} \w{1,};(\n {4}\w{1,} \w{1,};){0,}\n}( \w{1,}){0,1};")
    ],
    TypeLine.ENUM: [
        re.compile("^(typedef ){0,1}(enum )(\w{1,} ){0,1}{\n {4}\w{1,} \w{1,};(\n {4}\w{1,} \w{1,};){0,}\n}( \w{1,}){0,1};")
    ],
    TypeLine.GLOBAL: [
        re.compile("^(static ){0,1}(const ){0,1}\w{1,} \*{0,}\w{1,}(\[[0-9]{0,}\]){0,1} = ((\w{0,})|({\n{0,1} {0,}\w{0,}(,\n{0,1} {0,}\w{0,}){0,})|)\n{0,1}}{0,1};")
    ],
    TypeLine.FUNCTION: [
        re.compile("((static )|(const )){0,}\w{1,}(\*){0,} (\*){0,}\w{1,}\(((void)|(\n{0,1}.*( *\w{1,}){1,}(\*){0,} (\*){0,}\w{1,}(\[[0-9]{0,}\]){0,}(, {0,1}\n{0,1}( *\w{1,})(\*){0,} (\*){0,}\w{1,}(\[\d{0,}\]){0,}){0,3})\n{0,1} {0,})\)\n{0,1} {0,1}{\n(.*\n)*?}")
    ],
    TypeLine.FUNC_PROTO: [
        re.compile("((static )|(const )){0,}\w{1,}(\*){0,} (\*){0,}\w{1,}\(((void)|(\n{0,1}.*( *\w{1,}){1,}(\*){0,} (\*){0,}\w{1,}(\[[0-9]{0,}\]){0,}(, {0,1}\n{0,1}( *\w{1,})(\*){0,} (\*){0,}\w{1,}(\[\d{0,}\]){0,}){0,3})\n{0,1} {0,})\);")
    ]
}
