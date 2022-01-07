from source.file_parser import CFileParse
from source.file_parser import TypeLine
import os

def check(file: CFileParse) -> int:
    for char in os.path.basename(file.basename):
        if char in [chr(i) for i in range(ord('A'), ord('Z') + 1)]:
            print(f"{file.basename}: only lower case in file name")
            return 1
    return 0
