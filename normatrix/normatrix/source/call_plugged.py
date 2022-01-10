try:
    from normatrix.source import color
    from normatrix.source import file_parser
except ModuleNotFoundError:
    from normatrix.normatrix.source import color
    from normatrix.normatrix.source import file_parser

from importlib import import_module
from inspect import signature

def get_modules(list_checkers: list) -> list:
    checkers = []
    for mod in list_checkers:
        try:
            try:
                check = import_module(f'normatrix.plugged.{mod}')
            except ModuleNotFoundError:
                check = import_module(f'normatrix.normatrix.plugged.{mod}')
            sign = signature(check.check)
            if len(sign.parameters.keys()) != 1:
                raise ValueError
            checkers.append(check)
        except Exception as e:
            color.print_color("red", f"bad pluggin: plugged::{mod}::error::{e}")
    return checkers

def itter_mod(file: file_parser.CFileParse, checkers: list) -> (list, int):
    stats = []
    nb_error = 0
    for mod in checkers:
        info = (0, 3)
        try:
            info = mod.check(file)
        except Exception as e:
            print(f"ERROR: {mod.__name__}:{mod.__file__}: {e}")
        info_type = type(info).__name__
        if (info_type == "list" or info_type == "tuple") and \
                len(info) > 0 and type(info[0]).__name__ == "int":
            nb_error += info[0]
            if info[0] != 0 and len(info) > 1:
                errors = [(file.basename, 1, info[1]) for _ in range(info[0])]
                stats.extend(errors)
    return (stats, nb_error)

def call_plugged(files: list, list_checkers: list, pwd: str) -> (list, int):
    nb_error = 0
    stats = []
    checkers = get_modules(list_checkers)
    for i, file in enumerate(files):
        parse: file_parser.CFileParse = file_parser.parse(file, pwd)
        color.print_color("cyan", f"file [{parse.basename}] n°{i + 1}/{len(files)}...")
        curr_stat, last_nb_error = itter_mod(parse, checkers)
        if last_nb_error != 0:
            color.print_color("boldred", f" -> nope: {parse.basename} ({last_nb_error})")
            nb_error += last_nb_error
            stats.extend(curr_stat)
        else:
            color.print_color("green", f" -> yes: {parse.basename}")
    return (stats, nb_error)
