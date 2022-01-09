try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.file_parser import TypeLine
except:
    from normatrix.normatrix.source.file_parser import CFileParse
    from normatrix.normatrix.source.file_parser import TypeLine

import re

def check(file: CFileParse) -> (int, int):
    nb_error = 0
    for i in range(len(file.sub_parsedline)):
        line = file.sub_parsedline[i]
        if line[0] != TypeLine.COMMENT:
            ll = re.sub('\/\/.*', '', line[1])
            m = re.search(",\S", ll)
            if m != None:
                print(f"{file.basename}:{i + 1}: need a space after a comma ({ll[m.start():]})")
                nb_error += 1
    return (nb_error, 1)
