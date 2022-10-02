try:
    from normatrix.source.config import (
        BAD_FILE_EXTENSION,
        LIBC_BANNED_FUNC,
        OPERATOR_LIST,
    )
except ModuleNotFoundError:
    from src.normatrix.source.config import LIBC_BANNED_FUNC
    from src.normatrix.source.config import BAD_FILE_EXTENSION
    from src.normatrix.source.config import OPERATOR_LIST

import json
import os


def check_boolean(b) -> bool:
    if isinstance(b, bool):
        return b
    if isinstance(b, str):
        if b in ["yes", "y"]:
            return True
        else:
            return False
    return False


class Context:
    def __init__(
        self,
        path: str,
        only_error: str,
        output_format: str,
        no_fclean: bool = False,
        link_line: bool = False,
    ):
        self.LIBC_BANNED_FUNC = LIBC_BANNED_FUNC
        self.BAD_FILE_EXTENSION = BAD_FILE_EXTENSION
        self.OPERATOR_LIST = OPERATOR_LIST
        self.ENABLE_PREVIEW = False
        self.fclean_after = not check_boolean(no_fclean)
        self.link_line = check_boolean(link_line)
        self.only_error = check_boolean(only_error)
        if path:
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
            if self.only_error is False:
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
        if ret:
            self.ENABLE_PREVIEW = bool(ret)


def itter_remove(true_list: list, elems: list) -> None:
    if elems is None:
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
    if elems is None:
        return None
    try:
        for elem in elems:
            try:
                true_list.append(elem)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
