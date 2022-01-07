#!/usr/bin/env python3
import os
import sys
from source import file_parser
from source import color
from importlib import import_module

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

FILES_TO_CHECK = []
for root, _, files in os.walk(PWD):
    for file in files:
        filepath = os.path.join(root, file)
        ignore_normatrix = ('NorMatrix' in filepath and 'NorMatrix' in PWD) or \
                'NorMatrix' not in filepath
        ignore_folder = ('.git' not in filepath and '.vscode' not in filepath)
        if ignore_normatrix and ignore_folder and (file.endswith('.c') or file.endswith('.h')):
            FILES_TO_CHECK.append(filepath)

NB_ERROR = 0
STATS: list[tuple[str, int]] = []

color.print_color("green", "NorMatrix!")
color.print_color("cyan", f"directory to check: {PWD}\n")

for i in range(len(FILES_TO_CHECK)):
    file = FILES_TO_CHECK[i]
    LAST_NB_ERROR = 0
    parse: file_parser.CFileParse = file_parser.parse(file, PWD)
    color.print_color("cyan", f"file [{parse.basename}] n°{i + 1}/{len(FILES_TO_CHECK)}...")
    for checker_name in list_checkers:
        info = (0, 3)
        try:
            checker = import_module(f"plugged.{checker_name}")
            info = checker.check(parse)
        except Exception as e:
            print(f"ERROR: \n{e}")
        LAST_NB_ERROR += info[0]
        if info[0] != 0: STATS.extend([(parse.basename, 1, info[1]) for _ in range(info[0])])
    if LAST_NB_ERROR != 0:
        color.print_color("boldred", f" -> nope: {parse.basename} ({LAST_NB_ERROR})")
        NB_ERROR += LAST_NB_ERROR
    else:
        color.print_color("green", f" -> yes: {parse.basename}")

average = {}
for elem in STATS:
    if elem[0] not in average.keys():
        average[elem[0]] = elem[1]
    else:
        average[elem[0]] += elem[1]
average = sum(average.values()) / len(STATS)
nb_major = len([elem for elem in STATS if elem[2] == 0])
nb_minor = len([elem for elem in STATS if elem[2] == 1])
nb_info = len([elem for elem in STATS if elem[2] == 2])
color.print_color("cyan", f"\naverage number of error per file: {average}")
color.print_color("cyan", f"number of MAJOR: {nb_major} = {-3 * nb_major}")
color.print_color("cyan", f"number of MINOR: {nb_minor} = {-1 * nb_minor}")
color.print_color("cyan", f"number of INFO: {nb_info}")
color.print_color("cyan", f"note : {-3 * nb_major + -1 * nb_minor}")
color.print_color("cyan", f"number of file checked: {len(STATS)}")

if NB_ERROR == 0:
    color.print_color("green", "OK BRO")
    exit(0)
else:
    color.print_color("red", f"DUMB BRO ({NB_ERROR} error{'' if NB_ERROR == 0 else 's'})")
    exit(NB_ERROR)
