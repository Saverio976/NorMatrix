try:
    from normatrix.source import color
    from normatrix.source.context import Context
except ModuleNotFoundError:
    from src.normatrix.source import color
    from src.normatrix.source.context import Context

rich_present = False
try:
    from rich.table import Table
    from rich.console import Console
    rich_present = True
except:
    rich_present = False

def get_average_dict(stats: list) -> dict:
    average_dict = {}
    for elem in stats:
        if elem[0] not in average_dict.keys():
            average_dict[elem[0]] = elem[1]
        else:
            average_dict[elem[0]] += elem[1]
    return average_dict

def get_nb_error_categories(stats: list) -> (float, float, float):
    nb_major = len([elem for elem in stats if elem[2] == 0])
    nb_minor = len([elem for elem in stats if elem[2] == 1])
    nb_info = len([elem for elem in stats if elem[2] == 2])
    return (nb_major, nb_minor, nb_info)

def print_stats_md_html(context: Context, stats: list, files: list, nb_line: int) -> None:
    file = open(context.output_file, "a")
    average_dict = get_average_dict(stats)
    print(f"\n*number of files checked: {len(files)}*\n", file=file)
    print(f"*number of lines checked: {nb_line}*\n", file=file)
    average = sum(average_dict.values()) / len(files) if len(files) != 0 else 1
    print(f"*average number of error per file: {average:.2f}*", file=file)
    nb_major, nb_minor, nb_info = get_nb_error_categories(stats)
    print(f"***number of __MAJOR__: {nb_major} = {-3 * nb_major}***", file=file)
    print(f"***number of __MINOR__: {nb_major} = {-1 * nb_minor}***", file=file)
    print(f"***number of __INFO__: {nb_info} = -0***", file=file)
    note = -3 * nb_major + -1 * nb_minor
    if note == 0 or note == -0:
        print(f"**__note: -0__**", file=file)
    else:
        print(f"**__note: {note}__**", file=file)
    file.close()

def print_stats_rich(context: Context, stats: list, files: list, nb_line: int) -> None:
    average_dict = get_average_dict(stats)
    table = Table(title="[bold blue]STATS", expand=True)
    table.add_column("Value", no_wrap=True)
    table.add_column("Explanation", style="cyan", no_wrap=True)
    table.add_row(f"[cyan]{len(files)}", "files checked")
    table.add_row(f"[cyan]{nb_line}", "lines checked")
    average = sum(average_dict.values()) / len(files) if len(files) != 0 else 1
    def get_color(x: float):
        if average == 0:
            return "[green]"
        elif average < 1:
            return "[yellow]"
        else:
            return "[red]"
    table.add_row(f"{get_color(average)}{average:.2f}", "errors per file")
    nb_major, nb_minor, nb_info = get_nb_error_categories(stats)
    table.add_row(f"{get_color(nb_major)}{nb_major}", "major.s")
    table.add_row(f"{get_color(nb_minor)}{nb_minor}", "minor.s")
    table.add_row(f"{get_color(nb_info)}{nb_info}", "info.s")
    note = -3 * nb_major + -1 * nb_minor
    table.add_row(f"{get_color(note)}{note}", "to remove from your note")
    console = Console()
    console.print(table)

def print_stats_color(context: Context, stats: list, files: list, nb_line: int) -> None:
    average_dict = get_average_dict(stats)
    color.print_color("cyan", f"\nnumber of files checked: {len(files)}")
    color.print_color("cyan", f"number of lines checked: {nb_line}")
    average = sum(average_dict.values()) / len(files) if len(files) != 0 else 1
    color.print_color("cyan", f"average number of error per file: {average:.2f}")
    nb_major, nb_minor, nb_info = get_nb_error_categories(stats)
    color.print_color("red", f"number of MAJOR: {nb_major} = {-3 * nb_major}")
    color.print_color("blue", f"number of MINOR: {nb_minor} = {-1 * nb_minor}")
    color.print_color("green", f"number of INFO: {nb_info} = -0")
    note = -3 * nb_major + -1 * nb_minor
    if note == 0 or note == -0:
        color.print_color("green", "note: -0")
    else:
        color.print_color("red", f"note : {note}")

def print_stats(context: Context, stats: list, files: list, nb_line: int) -> None:
    if context.output_format in ["html", "md"]:
        print_stats_md_html(context, stats, files, nb_line)
    elif context.output_format == "term_rich" and rich_present == True:
        print_stats_rich(context, stats, files, nb_line)
    else:
        print_stats_color(context, stats, files, nb_line)
