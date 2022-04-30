try:
    from normatrix.source.context import Context
    from normatrix.source.color import print_color
except ModuleNotFoundError:
    from src.normatrix.source.context import Context
    from src.normatrix.source.color import print_color

rich_present = False
try:
    from rich.table import Table
    from rich.console import Console
    rich_present = True
except ModuleNotFoundError:
    rich_present = False

def print_right_format_md_html(context: Context, filepath: str, nb_total_err: int, list_error: list) -> None:
    file = open(context.output_file, "a")
    if context.only_error == False or nb_total_err != 0:
        print(f"**{filepath} | {nb_total_err} error.s**\n", file=file)
    for err_line, err_msg in list_error:
        print(f"- {err_line}: {err_msg}\n", file=file)
    print("\n", file=file)
    file.close()

def print_right_format_color(context: Context, filepath: str, nb_total_err: int, list_error: list) -> None:
    for err_line, err_msg in list_error:
        print(f"{err_line}: {err_msg}")
        if context.link_line == True:
            print(f"link : {filepath}:{err_line}")
    if nb_total_err != 0:
        print_color("red", f"-> nope [{filepath}]:[{nb_total_err} error.s]")
    elif context.only_error == False:
        print_color("green", f"-> yez [{filepath}]")

def print_right_format_rich(context: Context, filepath: str, nb_total_err: int, list_error: list) -> None:
    if nb_total_err == 0:
        return
    table = Table(title=f"[bold magenta]{filepath} [{nb_total_err} error.s]", expand=True)
    table.add_column("Lines", style="cyan", no_wrap=False)
    table.add_column("Error Message", style="red", no_wrap=True)
    dico = dict()
    for err_line, err_msg in list_error:
        if err_line in dico:
            dico[err_line].append(err_msg)
        else:
            dico[err_line] = [err_msg]
    sort_list = sorted(list(dico.items()), key = lambda x: x[0])
    for line, errors in sort_list:
        for i, err_msg in enumerate(errors):
            table.add_row(f"{line}" if i == 0 else '', f"{err_msg}")
    console = Console()
    console.print(table)
    if context.link_line == True:
        for err_line, _ in sort_list:
            print(f".. link : {filepath}:{err_line}")

def print_right_format(context: Context, filepath: str, nb_total_err: int, list_error: list) -> None:
    if context.output_format in ["html", "md"]:
        print_right_format_md_html(context, filepath, nb_total_err, list_error)
    elif context.output_format == "term_rich" and rich_present == True:
        print_right_format_rich(context, filepath, nb_total_err, list_error)
    else:
        print_right_format_color(context, filepath, nb_total_err, list_error)
