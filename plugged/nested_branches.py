from source.file_parser import CFileParse
from source.file_parser import TypeLine

def check(file: CFileParse) -> int:
    nb_error = 0
    in_switch = False
    for i in range(len(file.sub_parsedline)):
        line: str = file.sub_parsedline[i][1]
        if "switch " in line and " {\n" in line:
            in_switch = True
        if in_switch and "}\n" in line:
            in_switch = False
        if in_switch: condition = line.startswith(" " * 20)
        else: condition = line.startswith(" " * 15)
        if condition:
            can_continue = (line.startswith(" " * 16) and line.endswith(");\n")) \
                or line.endswith(") {\n") or ") ? " in line \
                or ") ? " in file.sub_parsedline[i - 1][1]
            if can_continue or (line.endswith(")\n") and (
                    "if (" in file.sub_parsedlines[i - 1][1] or
                    "while (" in file.sub_parsedlines[i - 1][1] or
                    "for (" in file.sub_parsedlines[i - 1][1])):
                continue
            print(f"{file.basename}:{i + 1}: maybe too many branch ?")
            nb_error += 1
    return nb_error
