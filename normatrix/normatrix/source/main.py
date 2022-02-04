import os
import sys
import argparse

try:
    from normatrix.source import color
    from normatrix.source import get_file_to_check
    from normatrix.source import print_stats
    from normatrix.source import call_plugged
    from normatrix import plugged
except ModuleNotFoundError:
    from normatrix.normatrix.source import color
    from normatrix.normatrix.source import get_file_to_check
    from normatrix.normatrix.source import print_stats
    from normatrix.normatrix.source import call_plugged
    from normatrix.normatrix import plugged

def call_argparse():
    parser = argparse.ArgumentParser(prog='python -m normatrix',
            description='The C Epitech Coding Style Norm Checker',
            epilog='source: https://github.com/Saverio976/NorMatrix')
    parser.add_argument('paths', metavar='paths', nargs='*',
            help='list of path to check (default: the current working directory)')
    parser.add_argument('--no-operators-pluggin', action='store_const',
            dest='plug_operator_activ', const='no', default='yes',
            help='remove the operators pluggin (because it print some false positiv for now)')
    parser.add_argument('--preview', action='store_const',
            dest='preview_plugins', const='yes', default='no',
            help='add some plugin that are added recently')
    result = parser.parse_args()
    if result.paths == []:
        result.paths.append(os.getcwd())
    return result

def check_norm_path(pwd: str, plug_operator_activ: bool, preview: bool) -> int:
    list_checkers = plugged.__all__
    if plug_operator_activ == False:
        list_checkers.remove('operators')
    if preview:
        list_checkers.extend(plugged.PREVIEW)

    color.print_color("green", "\nNorMatrix!")
    color.print_color("cyan", f"directory to check: {pwd}\n")

    stats, files_to_check = get_file_to_check.get_file_to_check(pwd)

    STATS, NB_ERROR = call_plugged.call_plugged(files_to_check, list_checkers, pwd)

    STATS.extend(stats)
    NB_ERROR += len(stats)

    print_stats.print_stats(STATS, files_to_check)

    if NB_ERROR == 0:
        color.print_color("green", "OK BRO")
        return 0
    else:
        color.print_color("red", f"DUMB BRO ({NB_ERROR} error{'' if NB_ERROR == 0 else 's'})")
        return NB_ERROR

def main():
    args = call_argparse()
    result = args
    ret_code = 0
    is_preview = result.preview_plugins == "yes"
    is_plugin_operator = result.plug_operator_activ == "yes"
    for path in result.paths:
        if check_norm_path(path, is_plugin_operator, is_preview) != 0:
            ret_code += 1
    if ret_code != 0:
        if len(result.paths) == 1:
            exit(1)
        print(f'\nYou Have {ret_code} folder that dont respect the norm')
        exit(1)
    exit(0)
