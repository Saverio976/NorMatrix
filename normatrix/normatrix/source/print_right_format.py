try:
    from normatrix.source.context import Context
    from normatrix.source.color import print_color
except ModuleNotFoundError:
    from normatrix.normatrix.source.context import Context
    from normatrix.normatrix.source.color import print_color

def print_right_format(context: Context, filepath: str, nb_total_err: int, list_error: list) -> None:
    if context.output_format in ["html", "md"]:
        file = open(context.output_file, "a")
        print(f"**{filepath} | {nb_total_err} error.s**", file=file)
    for err_line, err_msg in list_error:
        if context.output_format in ["html", "md"]:
            print(f"- {err_line}: {err_msg}", file=file)
        elif context.output_format == "term_color":
            print(f"{err_line}: {err_msg}")
    if context.output_format == "term_color":
        if nb_total_err != 0:
            print_color("red", f"-> nope [{filepath}]:[{nb_total_err} error.s]")
        elif context.only_error == False:
            print_color("green", f"-> yez [{filepath}]")
    if context.output_format in ["html", "md"]:
        print("", file=file)
        file.close()
