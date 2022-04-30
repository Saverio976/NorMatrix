import os
import sys
import argparse

try:
    from normatrix.source import color
    from normatrix.source import get_file_to_check
    from normatrix.source import print_stats
    from normatrix.source.context import Context
    from normatrix.source import call_plugged
    from normatrix.source import makefile
    from normatrix import plugged
    from normatrix.test.tests import run_tests
except ModuleNotFoundError:
    from src.normatrix.source import color
    from src.normatrix.source import get_file_to_check
    from src.normatrix.source import print_stats
    from src.normatrix.source.context import Context
    from src.normatrix.source import call_plugged
    from src.normatrix.source import makefile
    from src.normatrix import plugged
    from src.normatrix.test.tests import run_tests

FULL_DOC = """SOURCE:
    https://github.com/Saverio976/NorMatrix

UPDATE:
    - if you install it with 'pip'
        pip install -U normatrix
    - if you install it with git
        git pull
    - other method:
        (do it yourself)

CONFIGS:
    normatrix can read a special json file for configuration.
    -> put a `.normatrix.json` file on the path where tou execute normatrix
    -> and execute normatrix like you did it before

    default configuration file:
        ```json
        {
            "banned": ["printf", "memset", "strcpy", "strcat", "calloc"],
            "no-banned": [],
            "extension": [".a", ".o", ".so", ".gch", "~", "#", ".d"],
            "no-extension": [],
            "enable-preview": false
        }
        ```

    for further information read the README.md on
    https://github.com/Saverio976/NorMatrix
"""

list_options = [
    ['--no-operators-pluggin', 'plug_operator_activ', 'no', 'yes',
        'remove the operators pluggin (because it print some false positiv for now)'],
    ['--preview', 'preview_plugins', 'yes', 'no',
        'add some plugin that are added recently'],
    ['--conf', 'configs', 'yes', 'no',
        '[deprecated][now it check always for the file] tells if you have a .normatrix config file'],
    ['--only-errors', 'only_error', 'yes', 'no',
        'print only bad files with errors'],
    ['--no-fclean', 'no_fclean', True, False,
        'if you want normatrix dont do a "make fclean" at the end'],
    ['--link-line', 'link_line', True, False,
        'to have the "link" to the file (in vscode terminal you can click it and it will open the file at the line of the error)'],
    ['--tests-run', 'pass_test', True, False,
        'run the unit tests for normatrix']
]

def call_argparse():
    parser = argparse.ArgumentParser(prog='python -m normatrix',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='The C Epitech Coding Style Norm Checker',
            epilog=FULL_DOC)
    for options in list_options:
        parser.add_argument(options[0], action='store_const', dest=options[1],
            const=options[2], default=options[3], help=options[4])
    parser.add_argument('--output', metavar="format",
            choices=["html", "md", "term_color", "term_rich"],
            dest='output_format', default="term_rich",
            help='tell which output format to use [html, md, term_color, term_rich]; for html the file is normatrix-result.htlm; for md the file is normatrix-result.md')
    parser.add_argument('paths', metavar='paths', nargs='*',
            help='list of path to check (default: the current working directory)')
    result = parser.parse_args()
    if result.paths == []:
        result.paths.append(os.getcwd())
    return result

def check_norm_path(pwd: str, context: Context, plug_operator_activ: bool, preview: bool) -> int:
    list_checkers = plugged.__all__
    if plug_operator_activ == False:
        list_checkers.remove('operators')
    if preview or context.ENABLE_PREVIEW == True:
        list_checkers.extend(plugged.PREVIEW)

    if context.output_format in ["html", "md"]:
        with open(context.output_file, "a") as file:
            print("\n\n# NorMatrix!", file=file)
            print(f"## Directory: {pwd}", file=file)
            print("", file=file)
    elif context.output_format == "term_color":
        color.print_color("green", "\nNorMatrix!")
        color.print_color("cyan", f"directory to check: {pwd}\n")

    stats, files_to_check = get_file_to_check.get_file_to_check(context, pwd)

    STATS, NB_ERROR, nb_line = call_plugged.call_plugged(context, files_to_check, list_checkers, pwd)

    STATS.extend(stats)
    NB_ERROR += len(stats)

    print_stats.print_stats(context, STATS, files_to_check, nb_line)

    if NB_ERROR == 0:
        if context.output_format in ["html", "md"]:
            with open(context.output_file, "a") as file:
                print(f"## Directory: {pwd} is **OK**", file=file)
        elif context.output_format == "term_color":
            color.print_color("green", "OK BRO")
        return 0
    else:
        if context.output_format in ["html", "md"]:
            with open(context.output_file, "a") as file:
                print(f"## Directory: {pwd} is **BAD** with **{NB_ERROR}** error.s", file=file)
        elif context.output_format == "term_color":
            color.print_color("red", f"DUMB BRO ({NB_ERROR} error.s)")
        return NB_ERROR

def transform_to_html(context: Context):
    try:
        from markdown import Markdown
    except ModuleNotFoundError:
        print("you should install the markdown package first (pip install markdown)")
        exit(1)
    to_file = context.output_file.replace(".md", ".html")
    mark = Markdown()
    mark.convertFile(input=context.output_file, output=to_file)
    os.remove(context.output_file)
    with open(to_file, "r") as file:
        lines = file.readlines()
    lines.insert(0, "<!DOCTYPE html>")
    lines.insert(1, "<head>")
    lines.insert(2, "<title>NorMatrix Results</title>")
    lines.insert(3, "</head>")
    lines.insert(4, "<body>")
    lines.append("</body>")
    with open(to_file, "w") as file:
        file.writelines(lines)

def main():
    result = call_argparse()
    if result.pass_test == True:
        exit(run_tests())
    ret_code = 0
    is_preview = result.preview_plugins == "yes"
    is_plugin_operator = result.plug_operator_activ == "yes"
    for path in result.paths:
        curr_ret_code = 0
        context = Context(path, result.only_error, result.output_format, result.no_fclean, result.link_line)
        if check_norm_path(path, context, is_plugin_operator, is_preview) != 0:
            curr_ret_code += 1
        if makefile.check(context, path)[0] != 0:
            curr_ret_code += 1
        if curr_ret_code != 0:
            ret_code += 1
    if ret_code != 0:
        if context.output_format in ["html", "md"]:
            with open(context.output_file, "a") as file:
                print(f"\n# You Have {ret_code} folder.s that dont respect the norm", file=file)
        elif context.output_format == "term_color":
            print(f'\nYou Have {ret_code} folder.s that dont respect the norm')
    if result.output_format == "html":
        transform_to_html(context)
    exit(0 if ret_code == 0 else 1)
