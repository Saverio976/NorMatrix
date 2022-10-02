try:
    from normatrix.source.file_parser import CFileParse
except ModuleNotFoundError:
    from src.normatrix.source.file_parser import CFileParse

import os


def check(context, file: CFileParse) -> (int, int, list):
    if file.filepath.endswith("Makefile"):
        return (0, 0, [])
    for char in os.path.basename(file.basename):
        if char in [chr(i) for i in range(ord("A"), ord("Z") + 1)]:
            return (1, 0, [(0, "only lower case in file name")])
    return (0, 0, [])
