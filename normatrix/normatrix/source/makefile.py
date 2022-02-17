try:
    from normatrix.source import color
except ModuleNotFoundError:
    from normatrix.normatrix.source import color

import subprocess

def check(path: str) -> (int, int):
    nb_error = 0
    ret = subprocess.run(["make", "-C", path], capture_output=True)
    if ret.returncode != 0:
        print(ret.stderr.decode("utf-8"))
        color.print_color("red", "no makefile in this repo")
        return (0, 0)
    ret = subprocess.run(["find", path, "-maxdepth", "2", "-perm", "-a=x", "!", "(", "-type", "d", ")"], capture_output=True)
    if ret.returncode != 0:
        print(ret.stderr.decode("utf-8"))
        color.print_color("red", "cannot find executable.s")
        return (0, 0)
    all_exe = ret.stdout.decode("utf-8").split("\n")[:-1]
    for exe in all_exe:
        print("exe found :", str(exe))
    for exe in all_exe:
        ret = subprocess.run(["nm", exe], capture_output=True)
        if ret.returncode == 0:
            data = ret.stdout.decode("utf-8")
            if "memset" in data:
                color.print_color("red", f"memset found in {exe} (maybe you use clang to compile and it use memset for some optimisation)")
                nb_error += 1
            else:
                color.print_color("green", f"ok : {str(exe)}")
        else:
            print(ret.stderr.decode("utf-8"))
    return (nb_error, 0)
