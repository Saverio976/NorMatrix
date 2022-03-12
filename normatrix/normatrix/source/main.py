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
except ModuleNotFoundError:
    from normatrix.normatrix.source import color
    from normatrix.normatrix.source import get_file_to_check
    from normatrix.normatrix.source import print_stats
    from normatrix.normatrix.source.context import Context
    from normatrix.normatrix.source import call_plugged
    from normatrix.normatrix.source import makefile
    from normatrix.normatrix import plugged

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
    -> execute normatrix whit `--conf` command line argument

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

def call_argparse():
    parser = argparse.ArgumentParser(prog='python -m normatrix',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='The C Epitech Coding Style Norm Checker',
            epilog=FULL_DOC)
    parser.add_argument('paths', metavar='paths', nargs='*',
            help='list of path to check (default: the current working directory)')
    parser.add_argument('--no-operators-pluggin', action='store_const',
            dest='plug_operator_activ', const='no', default='yes',
            help='remove the operators pluggin (because it print some false positiv for now)')
    parser.add_argument('--preview', action='store_const',
            dest='preview_plugins', const='yes', default='no',
            help='add some plugin that are added recently')
    parser.add_argument('--conf', action='store_const',
            dest='configs', const='yes', default='no',
            help='tells if you have a .normatrix config file')
    parser.add_argument('--only-error', action='store_const',
            dest='only_error', const='yes', default='no',
            help='print only bad files with errors')
    parser.add_argument('--output', metavar="format",
            choices=["html", "md", "term_color"], dest='output_format',
            default="term_color",
            help='tell which output format to use [html, md, term_color]; for html the file is normatrix-result.htmk; for md the file is normatrix-result.md')
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

    stats, files_to_check = get_file_to_check.get_file_to_check(pwd)

    STATS, NB_ERROR = call_plugged.call_plugged(context, files_to_check, list_checkers, pwd)

    STATS.extend(stats)
    NB_ERROR += len(stats)

    print_stats.print_stats(context, STATS, files_to_check)

    if NB_ERROR == 0:
        if context.output_format in ["html", "md"]:
            with open(context.output_file, "a") as file:
                print("## Directory: {pwd} is **OK**", file=file)
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

def main():
    result = call_argparse()
    ret_code = 0
    is_preview = result.preview_plugins == "yes"
    is_plugin_operator = result.plug_operator_activ == "yes"
    for path in result.paths:
        curr_ret_code = 0
        if result.configs == "yes":
            context = Context(os.path.join(path, ".normatrix.json"), result.only_error, result.output_format)
        else:
            context = Context(None, result.only_error, result.output_format)
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
        try:
            from markdown import Markdown
        except ModuleNotFoundError:
            print("you should install the markdown package first (pip install markdown)")
            exit(1)
        mark = Markdown()
        mark.convertFile(input=context.output_file, output=context.output_file.replace(".md", ".html"))
        os.remove(context.output_file)
    exit(0 if ret_code == 0 else 1)
