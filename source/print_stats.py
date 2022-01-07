from source import color

def print_stats(stats: list, files: list):
    average_dict = {}
    for elem in stats:
        if elem[0] not in average_dict.keys():
            average_dict[elem[0]] = elem[1]
        else:
            average_dict[elem[0]] += elem[1]
    average = sum(average_dict.values()) / len(files)
    nb_major = len([elem for elem in stats if elem[2] == 0])
    nb_minor = len([elem for elem in stats if elem[2] == 1])
    nb_info = len([elem for elem in stats if elem[2] == 2])
    color.print_color("cyan", f"\nnumber of file checked: {len(files)}")
    color.print_color("cyan", f"average number of error per file: {average}")
    color.print_color("cyan", f"number of MAJOR: {nb_major} = {-3 * nb_major}")
    color.print_color("cyan", f"number of MINOR: {nb_minor} = {-1 * nb_minor}")
    color.print_color("cyan", f"number of INFO: {nb_info}")
    color.print_color("cyan", f"note : {-3 * nb_major + -1 * nb_minor}")

