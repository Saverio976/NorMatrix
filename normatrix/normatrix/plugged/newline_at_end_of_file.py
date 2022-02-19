try:
    from normatrix.source.file_parser import CFileParse
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse

def check(context, file: CFileParse) -> (int, int):
    if file.real_parsedline[-1][1] != "":
        print(f"{file.basename}: need a line break at end of file")
        return (1, 2)
    else:
        return (0, 2)
