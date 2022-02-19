try:
    from normatrix.source.file_parser import CFileParse
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse

def check_non_comment_line(file: CFileParse, line: str, i: int, IS_IN_COMMENT: bool, nb_error: int):
    separator = [chr(k) for k in range(ord('a'), ord('z')+1)] + \
                [chr(k) for k in range(ord('A'), ord('Z')+1)] + \
                [chr(k) for k in range(ord('0'), ord('9')+1)]
    line: str = line.split("//")[0]
    line = line.split("/*")
    if len(line) == 1:
        line: str = line[0]
        e = 0
        while e < len(line) and line[e] not in separator:
            e += 1
        try:
            line[e:].index("  ")
            nb_error += 1
            print(f"{file.basename}:{i + 1}: two space alone ({line[e:]})")
        except ValueError: pass
    else:
        IS_IN_COMMENT = True
    return (IS_IN_COMMENT, nb_error)

def check(context, file: CFileParse) -> (int, int):
    IS_IN_COMMENT = False
    nb_error = 0
    filelines = file.sub_filelines
    for i, line in enumerate(filelines):
        if IS_IN_COMMENT:
            try:
                line.index('*/')
                IS_IN_COMMENT = False
            except ValueError: pass
        else:
            IS_IN_COMMENT, nb_error = check_non_comment_line(file, line, i, IS_IN_COMMENT, nb_error)
    return (nb_error, 1)
