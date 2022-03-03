try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse
    from normatrix.normatrix.source.config import TypeLine

import re

def check(context, file: CFileParse) -> (int, int):
    nb_error = 0
    in_switch = False
    is_in_func = [False, False]
    for i in range(len(file.sub_parsedline)):
        line = file.sub_parsedline[i][1]
        line = re.sub("^( )*$", '', re.sub('\/\/.*', '', line))
        if not is_in_func[0] and file.sub_parsedline[i][0] == TypeLine.FUNCTION:
            is_in_func[0] = True
        if is_in_func[1] and file.sub_parsedline[i][0] != TypeLine.FUNCTION:
            is_in_func[0] = False
            is_in_func[1] = False
        if is_in_func[0] and line.startswith('{'):
            is_in_func[1] = True
        if is_in_func[1] and not line.startswith('}'):
            if "switch " in line and line.endswith(" {"):
                in_switch = True
            if in_switch and line.endswith(" }"):
                in_switch = False
            condition = line.startswith(" " * 20 if in_switch else " " * 15)
            if condition:
                can_continue = (line.startswith(" " * 16) and line.endswith(");")) or line.endswith(") {") or ") ? " in line or ") ? " in line
                can_continue = can_continue or (i != 0 and file.real_parsedline[i - 1][1].endswith("\\"))
                if can_continue or (line.endswith(")") and ("if (" in file.sub_parsedline[i - 1][1] or "while (" in file.sub_parsedline[i - 1][1] or "for (" in file.sub_parsedline[i - 1][1])):
                    continue
                print(f"{file.basename}:{i + 1}: maybe too many branch ?")
                nb_error += 1
    return (nb_error, 1)
