#!/usr/bin/env python3
import sys

try:
    from normatrix.source.main import main
except ModuleNotFoundError:
    from normatrix.normatrix.source.main import main

##############################################################################
# TESTS

try:
    from normatrix.source import color
    from normatrix.source import file_parser
    from normatrix import plugged
    from normatrix.source.context import Context
except ModuleNotFoundError:
    from normatrix.normatrix.source import color
    from normatrix.normatrix.source import file_parser
    from normatrix.normatrix.source.context import Context
    from normatrix.normatrix import plugged

from importlib import import_module
from inspect import signature

import os

def get_modules(list_checkers: list) -> list:
    checkers = []
    for mod in list_checkers:
        try:
            try:
                check = import_module(f'normatrix.plugged.{mod}')
            except ModuleNotFoundError:
                check = import_module(f'normatrix.normatrix.plugged.{mod}')
            sign = signature(check.check)
            if len(sign.parameters.keys()) != 2:
                raise ValueError
            checkers.append(check)
        except Exception as e:
            color.print_color("red", f"bad puggin: plugged/{mod}/{e}")
    return checkers

def get_parsed_files_for_tests(checker, pwd) -> list:
    true_files = []
    files = []
    files.append(os.path.basename(checker.__file__)[:-3])
    files.append(os.path.basename(checker.__file__)[:-3])
    if files[0] == "snake_case":
        files[0] = "test/bad_code/SnakeKase.c"
    else:
        files[0] = f"test/bad_code/{files[0]}.c"
    files[1] = f"test/ok_code/{files[1]}.c"
    if os.path.exists(files[0]):
        true_files.append(file_parser.parse(files[0], pwd))
    if os.path.exists(files[1]):
        true_files.append(file_parser.parse(files[1], pwd))
    return true_files

def check_with_mod(checker, pwd) -> (int, int):
    context = Context(None, "no", "term_color")
    for file in get_parsed_files_for_tests(checker, pwd):
        info = (0, 3)
        try:
            info = checker.check(context, file)
        except Exception as e:
            print(f"ERROR: {checker.__file__}: {e}")
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

def test_main():
    nb_ret = 0
    list_checkers = plugged.__all__
    checkers = get_modules(list_checkers)
    stats, nb_error = itter_mod(checkers, "")
    if nb_error == 0:
        color.print_color("green", "NorMatrix [OK]")
        nb_ret = 0
    else:
        color.print_color("boldred", "NorMatrix [FAILED]")
        for file in stats:
            color.print_color("red", f"{file}")
        nb_ret = 1
    list_checkers = plugged.PREVIEW
    checkers = get_modules(list_checkers)
    stats, nb_error = itter_mod(checkers, "")
    if nb_error == 0:
        color.print_color("green", "Normatrix[preview] [OK]")
    else:
        color.print_color("boldred", "NorMatrix[preview] [FAILED]")
        for file in stats:
            color.print_color("red", f"{file}")
    return nb_ret
##############################################################################

if len(sys.argv) > 1 and sys.argv[1] == "--tests-run":
    exit(test_main())
else:
    exit(main())
