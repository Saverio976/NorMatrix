try:
    from normatrix.source.config import TypeLine
    from normatrix.source.custom_regex import re_sub
    from normatrix.source.file_parser import CFileParse
except ModuleNotFoundError:
    from src.normatrix.source.config import TypeLine
    from src.normatrix.source.custom_regex import re_sub
    from src.normatrix.source.file_parser import CFileParse


def check(context, file: CFileParse) -> (int, int, list):
    nb_error = 0
    list_error = []
    list_ok = [
        "do",
        "while",
        "for",
        "return",
        "if",
        "switch",
        "+",
        "-",
        "/",
        "*",
        "%",
        "=",
        "&",
        "|",
        ":",
        "?",
        ",",
        ";",
        "<",
        ">",
        ")",
    ]

    if file.filepath.endswith("Makefile"):
        return (nb_error, 1, list_error)
    for i in range(len(file.sub_parsedline)):
        line = file.sub_parsedline[i]
        if line[0] != TypeLine.COMMENT:
            ll = re_sub(r"\/\/.*", "", line[1], timeout=0.1)
            if "){" in ll:
                list_error.append((i + 1, f"need a space between '){{' ({ll})"))
                nb_error += 1
        if line[0] == TypeLine.FUNCTION and context.ENABLE_PREVIEW:
            for e, char in enumerate(ll, start=1):
                if char == "(" and ll[e - 2] == " ":
                    found = 0
                    for to_check in list_ok:
                        if ll[e - len(to_check) - 2 : e] == f"{to_check} (":
                            found = 1
                        if to_check in ["&", "*"]:
                            found = 1
                    if ll.strip().startswith("("):
                        found = 1
                    if found == 0:
                        list_error.append(
                            (i + 1, f"no need space when function call ({ll})")
                        )
                        nb_error += 1
                if char == "(" and ll[e - 2] != " ":
                    found = 0
                    for to_check in list_ok:
                        if ll[
                            e - len(to_check) - 1 : e
                        ] == f"{to_check}(" and to_check not in ["*", "&"]:
                            list_error.append(
                                (i + 1, f"need space for {to_check} ({ll})")
                            )
                            nb_error += 1
    return (nb_error, 1, list_error)
