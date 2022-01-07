import os

def get_file_to_check(path: str) -> list:
    files_to_check = []
    for root, _, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            ignore_normatrix = ('NorMatrix' in filepath and 'NorMatrix' in path) or \
                    'NorMatrix' not in filepath
            ignore_folder = '.git' not in filepath and '.vscode' not in filepath
            if ignore_normatrix and ignore_folder and (file.endswith('.c') or file.endswith('.h')):
                files_to_check.append(filepath)
    return files_to_check
