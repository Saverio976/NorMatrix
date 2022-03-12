try:
    from normatrix.source.config import LIBC_BANNED_FUNC
    from normatrix.source.config import BAD_FILE_EXTENSION
    from normatrix.source.config import OPERATOR_LIST
except ModuleNotFoundError:
    from normatrix.normatrix.source.config import LIBC_BANNED_FUNC
    from normatrix.normatrix.source.config import BAD_FILE_EXTENSION
    from normatrix.normatrix.source.config import OPERATOR_LIST

import json
import os

class Context:
    def __init__(self, path: str, only_error: str, output_format: str):
        self.LIBC_BANNED_FUNC = LIBC_BANNED_FUNC
        self.BAD_FILE_EXTENSION = BAD_FILE_EXTENSION
        self.OPERATOR_LIST = OPERATOR_LIST
        self.ENABLE_PREVIEW = False
        self.only_error = True if only_error == 'yes' else False
        if path != None:
            self.set_from_file(os.path.join(path, ".normatrix.json"))
            self.remove_gitignore(os.path.join(path, ".gitignore"))
        self.output_format = output_format
        if output_format in ["html", "md"]:
            self.output_file = "normatrix-result.md"
            file = open(self.output_file, "w")
            file.close()

    def remove_gitignore(self, gitignore_path: str):
        try:
            with open(gitignore_path, "r") as file:
                data = file.readlines()
        except Exception:
            return
        for line in data:
            ll = line.strip()
            ll = ll.replace("\n", "")
            ll = ll[1:] if ll.startswith("*") else ll
            if self.only_error == False:
                print(f"ignore bad extension : {ll}")
            if ll in self.BAD_FILE_EXTENSION:
                self.BAD_FILE_EXTENSION.remove(ll)

    def set_from_file(self, path):
        try:
            with open(path, "r") as file:
                data = json.load(file)
        except Exception:
            return None
        ret = data.get("banned", None)
        itter_append(self.LIBC_BANNED_FUNC, ret)
        ret = data.get("no-banned", None)
        itter_remove(self.LIBC_BANNED_FUNC, ret)
        ret = data.get("extension", None)
        itter_append(self.BAD_FILE_EXTENSION, ret)
        ret = data.get("no-extension", None)
        itter_remove(self.BAD_FILE_EXTENSION, ret)
        ret = data.get("enable-preview", None)
        if ret != None:
            self.ENABLE_PREVIEW = bool(ret)

def itter_remove(true_list: list, elems: list) -> None:
    if elems == None:
        return None
    try:
        for elem in elems:
            try:
                true_list.remove(elem)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

def itter_append(true_list: list, elems: list) -> None:
    if elems == None:
        return None
    try:
        for elem in elems:
            try:
                true_list.append(elem)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
