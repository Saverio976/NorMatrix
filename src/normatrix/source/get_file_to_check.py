try:
    from normatrix.source import color
    from normatrix.source.context import Context
    from normatrix.source.custom_regex import re_search
except ModuleNotFoundError:
    from src.normatrix.source import color
    from src.normatrix.source.context import Context
    from src.normatrix.source.custom_regex import re_search

import os

def check_is_file_has_bad_extension(context: Context, file: str) -> (bool, str):
    for elem in context.BAD_FILE_EXTENSION:
        if elem.startswith("*."):
            elem = elem.replace("*.", ".*\.", 1)
        elif elem.startswith("*"):
            elem = elem.replace("*",".*")
        if re_search(elem, file) != None:
            return (True, elem)
    return (False, "")

def get_file_to_check(context: Context, path: str) -> (list, list):
    stats = []
    files_to_check = []

    for root, _, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            ignore_normatrix = 'NorMatrix' not in filepath or \
                    ('NorMatrix' in filepath and 'NorMatrix' in path)
            ignore_folder = '.git/' not in filepath and \
                    '.vscode/' not in filepath and \
                    'tests/' not in filepath
            is_file_to_check = file.endswith('.c') or file.endswith('.h') or \
                    file == "Makefile"
            if ignore_normatrix and ignore_folder and is_file_to_check:
                files_to_check.append(filepath)
            elif ignore_normatrix and ignore_folder:
                if_check, bad_ext = check_is_file_has_bad_extension(context, file)
                if if_check:
                    print(f"{filepath}: bad extension ({bad_ext})")
                    color.print_color("boldred", f" -> nope {filepath} (1)")
                    stats.append((filepath, 1, 0))
    return (stats, files_to_check)
