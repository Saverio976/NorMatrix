try:
    from normatrix.source.file_parser import CFileParse
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse

def check(context, file: CFileParse) -> (int, int, list):
    if file.real_parsedline[-1][1] != "":
        return (1, 2, [(len(file.real_parsedline), "need a line break at end of file")])
    else:
        return (0, 2, [])
