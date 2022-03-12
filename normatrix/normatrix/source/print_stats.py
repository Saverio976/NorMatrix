try:
    from normatrix.source import color
    from normatrix.source.context import Context
except ModuleNotFoundError:
    from normatrix.normatrix.source import color
    from normatrix.normatrix.source.context import Context

def print_stats(context: Context, stats: list, files: list) -> None:
    file = ""
    if context.output_format in ["html", "md"]:
        file = open(context.output_file, "a")
    average_dict = {}
    for elem in stats:
        if elem[0] not in average_dict.keys():
            average_dict[elem[0]] = elem[1]
        else:
            average_dict[elem[0]] += elem[1]
    nb_major = len([elem for elem in stats if elem[2] == 0])
    nb_minor = len([elem for elem in stats if elem[2] == 1])
    nb_info = len([elem for elem in stats if elem[2] == 2])
    if context.output_format in ["html", "md"]:
        print(f"\n*number of file checked: {len(files)}*", file=file)
    elif context.output_format == "term_color":
        color.print_color("cyan", f"\nnumber of file checked: {len(files)}")
    if len(files) != 0:
        average = sum(average_dict.values()) / len(files)
        if context.output_format in ["html", "md"]:
            print(f"*average number of error per file: {average}*", file=file)
        elif context.output_format == "term_color":
            color.print_color("cyan", f"average number of error per file: {average}")
    if context.output_format in ["html", "md"]:
        print(f"***number of __MAJOR__: {nb_major} = {-3 * nb_major}***", file=file)
        print(f"***number of __MINOR__: {nb_major} = {-1 * nb_minor}***", file=file)
        print(f"***number of __INFO__: {nb_info} = 0***", file=file)
    elif context.output_format == "term_color":
        color.print_color("red", f"number of MAJOR: {nb_major} = {-3 * nb_major}")
        color.print_color("blue", f"number of MINOR: {nb_minor} = {-1 * nb_minor}")
        color.print_color("green", f"number of INFO: {nb_info} = 0")
    note = -3 * nb_major + -1 * nb_minor
    if note == 0 or note == -0:
        if context.output_format in ["html", "md"]:
            print(f"**__note: -0__**", file=file)
        elif context.output_format == "term_color":
            color.print_color("green", "note: -0")
    else:
        if context.output_format in ["html", "md"]:
            print(f"**__note: {note}__**", file=file)
        elif context.output_format == "term_color":
            color.print_color("red", f"note : {note}")
    if context.output_format in ["html", "md"]:
        file.close()
