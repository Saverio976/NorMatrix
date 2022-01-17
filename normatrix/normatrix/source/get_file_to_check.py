try:
    from normatrix.source import color
    from normatrix.source.config import BAD_FILE_EXTENSION
except ModuleNotFoundError:
    from normatrix.normatrix.source import color
    from normatrix.normatrix.source.config import BAD_FILE_EXTENSION

import os

def check_is_file_has_bad_extension(file: str) -> (bool, str):
    for elem in BAD_FILE_EXTENSION:
        if file.endswith(elem):
            return (True, elem)
    return (False, "")

def get_file_to_check(path: str) -> (list, list):
    stats = []
    files_to_check = []
    for root, _, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            ignore_normatrix = ('NorMatrix' in filepath and 'NorMatrix' in path) or \
                    'NorMatrix' not in filepath
            ignore_folder = '.git/' not in filepath and '.vscode/' not in filepath and \
                    'tests/' not in filepath
            if ignore_normatrix and ignore_folder and (file.endswith('.c') or file.endswith('.h')):
                files_to_check.append(filepath)
            elif ignore_normatrix and ignore_folder:
                if_check, bad_ext = check_is_file_has_bad_extension(file)
                if if_check:
                    print(f"{filepath}: bad extension ({bad_ext})")
                    color.print_color("boldred", f" -> nope {filepath} (1)")
                    stats.append((filepath, 1, 0))
    return (stats, files_to_check)
