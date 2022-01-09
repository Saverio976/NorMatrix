import os
import sys

from importlib import import_module

try:
    from normatrix.source import file_parser
    from normatrix.source import color
    from normatrix.source import get_file_to_check
    from normatrix.source import print_stats
    from normatrix.source import call_plugged
    from normatrix import plugged
except:
    from normatrix.normatrix.source import file_parser
    from normatrix.normatrix.source import color
    from normatrix.normatrix.source import get_file_to_check
    from normatrix.normatrix.source import print_stats
    from normatrix.normatrix.source import call_plugged
    from normatrix.normatrix import plugged

def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "tests_run":
            from tests.fn_tests import tests
            exit(tests.main())

    PWD: str = os.environ.get('PWD', None)
    if PWD == None:
        exit(84)

    NORMATRIX_SOURCE = os.path.dirname(sys.argv[0])
    if NORMATRIX_SOURCE == '':
        NORMATRIX_SOURCE = '.'
    os.chdir(NORMATRIX_SOURCE)
    list_checkers = plugged.__all__

    color.print_color("green", "NorMatrix!")
    color.print_color("cyan", f"directory to check: {PWD}\n")

    FILES_TO_CHECK = get_file_to_check.get_file_to_check(PWD)

    NB_ERROR = 0
    STATS = []

    STATS, NB_ERROR = call_plugged.call_plugged(FILES_TO_CHECK, list_checkers, PWD)

    print_stats.print_stats(STATS, FILES_TO_CHECK)

    if NB_ERROR == 0:
        color.print_color("green", "OK BRO")
        exit(0)
    else:
        color.print_color("red", f"DUMB BRO ({NB_ERROR} error{'' if NB_ERROR == 0 else 's'})")
        exit(NB_ERROR)
