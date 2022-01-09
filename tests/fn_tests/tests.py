from source import color
from source import file_parser

from importlib import import_module
from inspect import signature

import os

def get_modules(list_checkers: list) -> list:
    checkers = []
    for mod in list_checkers:
        try:
            check = import_module(f'plugged.{mod}')
            sign = signature(check.check)
            if len(sign.parameters.keys()) != 1:
                raise ValueError
            checkers.append(check)
        except:
            color.print_color("red", f"bad puggin: pplugged/{mod}")
    return checkers

def get_parsed_files_for_tests(checker, pwd) -> list:
    true_files = []
    files = []
    files.append(os.path.basename(checker.__file__)[:-3])
    files.append(os.path.basename(checker.__file__)[:-3])
    if files[0] == "snake_case":
        files[0] = f"tests/bad_code/SnakeKase.c"
    else:
        files[0] = f"tests/bad_code/{files[0]}.c"
    files[1] = f"tests/ok_code/{files[1]}.c"
    if os.path.exists(files[0]):
        true_files.append(file_parser.parse(files[0], pwd))
    if os.path.exists(files[1]):
        true_files.append(file_parser.parse(files[1], pwd))
    return true_files

def check_with_mod(checker, pwd) -> (int, int):
    for file in get_parsed_files_for_tests(checker, pwd):
        info = (0, 3)
        try:
            info = checker.check(file)
        except Exception as e:
            print(f"ERROR: {e}")
        info_type = type(info).__name__
        if (info_type == "list" or info_type == "tuple") and \
                len(info) > 0 and type(info[0]).__name__ == "int":
            if len(info) > 1:
                if "bad_code" in file.basename and info[0] == 0:
                    print("so bad")
                    raise ValueError
                if "ok_code" in file.basename and info[0] != 0:
                    print("so not not bad")
                    raise ValueError
            else:
                raise ValueError
        else:
            raise ValueError
    return (0, 0)

def itter_mod(checkers: list, pwd) -> (list, int):
    stats = []
    nb_error = 0
    for mod in checkers:
        try:
            check_with_mod(mod, pwd)
        except Exception as e:
            print(e)
            nb_error += 1
            stats.append(mod.__file__)
    return (stats, nb_error)

def main():
    pwd = ""
    list_checkers = []
    for file in os.listdir('plugged'):
        if file.endswith('.py'):
            list_checkers.append(file[:-3])
    checkers = get_modules(list_checkers)
    stats, nb_error = itter_mod(checkers, pwd)
    if nb_error == 0:
        color.print_color("green", "NorMatrix [OK]")
        return 0
    else:
        color.print_color("boldred", "NorMatrix [FAILED]")
        for file in stats:
            color.print_color("red", f"{file}")
        return 1