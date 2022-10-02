from enum import Enum

try:
    from normatrix.source.custom_regex import re_compile
except ModuleNotFoundError:
    from src.normatrix.source.custom_regex import re_compile

LIBC_BANNED_FUNC = ["printf", "memset", "strcpy", "strcat", "calloc", "fprintf"]

BAD_FILE_EXTENSION = ["*.a", "*.o", "*.so", "*.gch", "*~", "*#", "*.d"]

smart_match = {
    ":ALL:": ".",
    ":NOTHING:": "{0}",
    ":ALPHANUM:": "[0-9a-zA-Z]",
    ":NUM:": "[0-9]",
    ":ALPHA:": "[a-zA-Z]",
    ":NOSPACE:": r"\S",
}

OPERATOR_LIST = [
    (" ([+", "+", "+])= ", r"(\+\+\w)|(\w\+\+)"),
    (" ([-{", "-", "-])=> ", r"(--\w)|(\w--)"),
    (" ([/*", "*", ":NOTHING:", r"[\[\{\( ]\*{2,}"),
    (" (/*", "/", "*/= ", r'(<.*?\/.*?\.h>)|(".*?\/.*?\.h")'),
    ("< ", "<", ":ALL:"),
    (":ALL:", ">", " >="),
    (" ({[", "&", ":NOTHING:", "&&"),
    ("([ ", "!", ":ALL:"),
    ("/+*-=! ", "=", "= "),
    (":ALL:", "(", ":ALL:"),
    (":ALL:", ")", "}]) ;", r"\)\)"),
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
        re_compile(r"^( ){0,}?\/\*(.*?\n{0,}){0,}\*\/"),
        re_compile(r"^( ){0,}?\/\/.*"),
    ],
    TypeLine.MACRO: [re_compile(r"^ {0,}#\w{1,}.*")],
    TypeLine.STRUCT: [
        re_compile(
            r"^(typedef ){0,1}(struct )(\w{1,} ){0,1}{\n {4}\w{1,} "
            r"\w{1,};(\n {4}\w{1,} \w{1,};){0,}\n}( \w{1,}){0,1};"
        )
    ],
    TypeLine.ENUM: [
        re_compile(
            r"^(typedef ){0,1}(enum )(\w{1,} ){0,1}{\n {4}\w{1,} "
            r"\w{1,};(\n {4}\w{1,} \w{1,};){0,}\n}( \w{1,}){0,1};"
        )
    ],
    TypeLine.GLOBAL: [
        re_compile(
            r"^(static ){0,1}(const ){0,1}\w{1,} \*{0,}\w{1,}"
            r"(\[[0-9]{0,}\]){0,1} = ((\w{0,})|({\n{0,1} {0,}\w{0,}(,\n{0,1}"
            r" {0,}\w{0,}){0,})|)\n{0,1}}{0,1};"
        )
    ],
    TypeLine.FUNCTION: [
        re_compile(
            r"((static )|(const )){0,}\w{1,}(\*){0,} (\*){0,}\w{1,}\(((void)|"
            r"(\n{0,1}.*( *\w{1,}){1,}(\*){0,} (\*){0,}\w{1,}(\[[0-9]{0,}\]){0,}"
            r"(, {0,1}\n{0,1}\s*(\_\_\w*\_\_\(\(\w*\)\)){0,}( *\w{1,})(\*){0,} "
            r"(\*){0,}\w{1,}(\[\d{0,}\]){0,}){0,3})\n{0,1} {0,})\)\n{0,1} {0,1}"
            r"{\n(.*\n)*?}"
        )
    ],
    TypeLine.FUNC_PROTO: [
        re_compile(
            r"((static )|(const )){0,}\w{1,}(\*){0,} (\*){0,}\w{1,}\(((void)"
            r"|(\n{0,1}.*( *\w{1,}){1,}(\*){0,} (\*){0,}\w{1,}(\[[0-9]{0,}\]){0,}"
            r"(, {0,1}\n{0,1}( *\w{1,})(\*){0,} (\*){0,}\w{1,}(\[\d{0,}\]){0,}){0,3})"
            r"\n{0,1} {0,})\);"
        )
    ],
}
