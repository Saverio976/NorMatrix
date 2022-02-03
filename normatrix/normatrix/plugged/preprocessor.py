try:
    from normatrix.source.file_parser import CFileParse
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse

def check(file: CFileParse) -> (int, int):
    nb_error = 0
    TAB_NB = 0
    filelines = file.sub_filelines
    for i, line in enumerate(filelines):
        if " ".join(line.split()).startswith("#if"):
            TAB_NB += 4
        elif " ".join(line.split()).startswith("#endif"):
            TAB_NB -= 4
        elif " ".join(line.split()).startswith('#') and not line.startswith(" " * TAB_NB):
            print(f"{file.basename}:{i + 1}: #... need 4 space after an #if ({line})")
            nb_error += 1
        if TAB_NB < 0:
            print(f"{file.basename}:{i + 1}: need an #if.. before an #endif ({line})")
            nb_error += 1
            TAB_NB = 0
        if " ".join(line.split()).startswith('#define') and file.basename.endswith('.c'):
            print(f"{file.basename}:{i + 1}: no define in .c ({line})")
            nb_error += 1
    return (nb_error, 1)
