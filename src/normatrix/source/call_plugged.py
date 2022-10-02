try:
    from normatrix.source import color, file_parser, print_right_format
    from normatrix.source.context import Context
except ModuleNotFoundError:
    from src.normatrix.source import color
    from src.normatrix.source.context import Context
    from src.normatrix.source import file_parser
    from src.normatrix.source import print_right_format

from importlib import import_module
from inspect import signature


def get_modules(list_checkers: list) -> list:
    checkers = []
    for mod in list_checkers:
        try:
            try:
                check = import_module(f"normatrix.plugged.{mod}")
            except ModuleNotFoundError:
                check = import_module(f"src.normatrix.plugged.{mod}")
            sign = signature(check.check)
            if len(sign.parameters.keys()) != 2:
                raise ValueError
            checkers.append(check)
        except Exception as e:
            color.print_color("red", f"bad pluggin: plugged::{mod}::error::{e}")
    return checkers


def itter_mod(
    context: Context, file: file_parser.CFileParse, checkers: list
) -> (list, int):
    stats = []
    nb_error = 0
    list_error = []
    for mod in checkers:
        info = (0, 3)
        try:
            info = mod.check(context, file)
        except Exception as e:
            print(f"ERROR: {mod.__name__}:{mod.__file__}: {e}")
        info_type = type(info).__name__
        if (
            (info_type == "list" or info_type == "tuple")
            and len(info) > 0
            and type(info[0]).__name__ == "int"
        ):
            nb_error += info[0]
            if info[0] != 0 and len(info) > 1:
                errors = [(file.basename, 1, info[1]) for _ in range(info[0])]
                stats.extend(errors)
                if len(info) > 2:
                    list_error.extend(info[2])
    print_right_format.print_right_format(context, file.filepath, nb_error, list_error)
    return (stats, nb_error)


def call_plugged(
    context: Context, files: list, list_checkers: list, pwd: str
) -> (list, int):
    nb_error = 0
    stats = []
    nb_files_total = len(files)
    checkers = get_modules(list_checkers)
    nb_total_line = 0

    for i, file in enumerate(files):
        if context.only_error is False:
            color.print_color("cyan", f"file [{file}] n°{i + 1}/{nb_files_total}...")
        parse, nb_line = file_parser.parse(file, pwd)
        nb_total_line += nb_line
        curr_stat, last_nb_error = itter_mod(context, parse, checkers)
        if last_nb_error != 0:
            nb_error += last_nb_error
            stats.extend(curr_stat)
    return (stats, nb_error, nb_total_line)
