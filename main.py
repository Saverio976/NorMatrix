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
NB_LAST_ERROR = 0

color.print_color("green", "NorMatrix!")
color.print_color("cyan", f"directory to check: {PWD}\n")

for i in range(len(FILES_TO_CHECK)):
    file = FILES_TO_CHECK[i]
    NB_LAST_ERROR = 0
    parse: file_parser.CFileParse = file_parser.parse(file, PWD)
    color.print_color("cyan", f"file [{parse.basename}] n°{i + 1}/{len(FILES_TO_CHECK)}...")
    for checker_name in list_checkers:
        try:
            checker = import_module(f"plugged.{checker_name}")
            NB_LAST_ERROR += checker.check(parse)
        except Exception as e:
            print(f"ERROR: \n{e}")
    NB_ERROR += NB_LAST_ERROR
    if NB_LAST_ERROR != 0:
        color.print_color("boldred", f" -> nope: {parse.basename} ({NB_LAST_ERROR})")
    else:
        color.print_color("green", f" -> yes: {parse.basename}")

if NB_ERROR == 0:
    color.print_color("green", "OK BRO")
    exit(0)
else:
    color.print_color("red", f"DUMB BRO ({NB_ERROR} error{'' if NB_ERROR == 0 else 's'})")
    exit(NB_ERROR)
