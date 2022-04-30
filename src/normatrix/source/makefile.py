try:
    from normatrix.source import color
    from normatrix.source.context import Context
except ModuleNotFoundError:
    from src.normatrix.source import color
    from src.normatrix.source.context import Context

import os
import sys
import subprocess

#thanks to https://stackoverflow.com/a/234329
def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

def compile(path: str) -> bool:
    ret = subprocess.run(["make", "-C", path], capture_output=True)
    if ret.returncode != 0:
        print(ret.stderr.decode("utf-8"))
        color.print_color("red", "no makefile in this repo")
        return False
    return True

def get_all_exe(path: str) -> list:
    list_of_file = []
    remove_suffix = [".png", ".jpg", ".sh"]
    for root, dirs, files in walklevel(path, level=2):
        list_of_file.extend([os.path.join(root, cur) for cur in files
            if os.access(os.path.join(path, cur), os.X_OK)])
    list_of_file_tmp = []
    for file in list_of_file:
        is_ok = True
        for suffix in remove_suffix:
            if file.endswith(suffix):
                is_ok = False
        if is_ok:
            list_of_file_tmp.append(file)
    list_of_file = list_of_file_tmp
    return list_of_file

def check_funcs(context: Context, exe: str) -> int:
    nb_error = 0
    ret = subprocess.run(["nm", exe], capture_output=True)
    if ret.returncode != 0:
        sys.stderr.write("can't access info needed to read the binary\n")
        return 0
    data = ret.stdout.decode("utf-8")
    for func in context.LIBC_BANNED_FUNC:
        if f" {func}@" in data or f" {func} " in data:
            color.print_color("red", f"{func}: found in {exe}")
            if func == "memset":
                print("maybe you use clang to compile and it use memset for some optimisation")
            nb_error += 1
    if nb_error == 0:
        color.print_color("green", f"ok : {exe}")
    return nb_error

def fclean(context: Context, path: str):
    if context.fclean_after == False:
        return None
    ret = subprocess.run(["make", "-C", path, "fclean"], capture_output=True);
    if ret.returncode != 0:
        sys.stderr.write("can't execute 'make fclean' or an error append in 'make fclean'\n")

def check(contex: Context, path: str) -> (int, int):
    nb_error = 0
    if compile(path) == False:
        return (0, 0)
    all_exe = get_all_exe(path)
    if all_exe == None:
        return (0, 0)
    for exe in all_exe:
        color.print_color("cyan", f"exe found : {str(exe)}")
        nb_error += check_funcs(contex, exe)
    fclean(contex, path)
    return (nb_error, 0)
