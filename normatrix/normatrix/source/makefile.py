try:
    from normatrix.source import color
    from normatrix.source.context import Context
except ModuleNotFoundError:
    from normatrix.normatrix.source import color
    from normatrix.normatrix.source.context import Context

import subprocess

def compile(path: str) -> bool:
    ret = subprocess.run(["make", "-C", path], capture_output=True)
    if ret.returncode != 0:
        print(ret.stderr.decode("utf-8"))
        color.print_color("red", "no makefile in this repo")
        return False
    return True

def get_all_exe(path: str) -> list:
    ret = subprocess.run(["find", path, "-maxdepth", "2", "-perm", "-a=x", "!", "(", "-type", "d", ")"], capture_output=True)
    if ret.returncode != 0:
        print(ret.stderr.decode("utf-8"))
        color.print_color("red", "cannot find executable.s")
        return None
    all_exe = ret.stdout.decode("utf-8").split("\n")[:-1]
    return all_exe

def check_funcs(context: Context, exe: str) -> int:
    nb_error = 0
    ret = subprocess.run(["nm", exe], capture_output=True)
    if ret.returncode != 0:
        print(ret.stderr.decode("utf-8"))
        return 0
    data = ret.stdout.decode("utf-8")
    for func in context.LIBC_BANNED_FUNC:
        if f" {func}" in data:
            color.print_color("red", f"{func} found in {exe}")
            if func == "memset":
                print("maybe you use clang to compile and it use memset for some optimisation")
            nb_error += 1
    if nb_error == 0:
        color.print_color("green", f"ok : {exe}")
    return nb_error

def fclean(path: str):
    ret = subprocess.run(["make", "-C", path, "fclean"], capture_output=True);
    if ret.returncode != 0:
        print(ret.stderr.decode("utf-8"))

def check(contex: Context, path: str) -> (int, int):
    nb_error = 0
    if compile(path) == False:
        return (0, 0)
    all_exe = get_all_exe(path)
    if all_exe == None:
        return (0, 0)
    for exe in all_exe:
        print("exe found :", str(exe))
    for exe in all_exe:
        nb_error += check_funcs(contex, exe)
    fclean(path)
    return (nb_error, 0)
