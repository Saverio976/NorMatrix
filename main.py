#!/usr/bin/env python3
import os
import sys

from importlib import import_module

from source import file_parser
from source import color
from source import get_file_to_check
from source import print_stats
from source import call_plugged

PWD: str = os.environ.get('PWD', None)
if PWD == None:
    exit(84)

NORMATRIX_SOURCE = os.path.dirname(sys.argv[0])
if NORMATRIX_SOURCE == '':
    NORMATRIX_SOURCE = '.'
os.chdir(NORMATRIX_SOURCE)
list_checkers = []
for file in os.listdir('plugged'):
    if file.endswith('.py'):
        list_checkers.append(file[:-3])

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
