try:
    from normatrix.source import color
except ModuleNotFoundError:
    from normatrix.normatrix.source import color

def print_stats(stats: list, files: list) -> None:
    average_dict = {}
    for elem in stats:
        if elem[0] not in average_dict.keys():
            average_dict[elem[0]] = elem[1]
        else:
            average_dict[elem[0]] += elem[1]
    nb_major = len([elem for elem in stats if elem[2] == 0])
    nb_minor = len([elem for elem in stats if elem[2] == 1])
    nb_info = len([elem for elem in stats if elem[2] == 2])
    color.print_color("cyan", f"\nnumber of file checked: {len(files)}")
    if len(files) != 0:
        average = sum(average_dict.values()) / len(files)
        color.print_color("cyan", f"average number of error per file: {average}")
    color.print_color("red", f"number of MAJOR: {nb_major} = {-3 * nb_major}")
    color.print_color("blue", f"number of MINOR: {nb_minor} = {-1 * nb_minor}")
    color.print_color("green", f"number of INFO: {nb_info} = -0")
    note = -3 * nb_major + -1 * nb_minor
    if note == 0 or note == -0:
        color.print_color("green", "note: -0")
    else:
        color.print_color("red", f"note : {note}")
