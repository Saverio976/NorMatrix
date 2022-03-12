try:
    from normatrix.source.config import LIBC_BANNED_FUNC
    from normatrix.source.config import BAD_FILE_EXTENSION
    from normatrix.source.config import OPERATOR_LIST
except ModuleNotFoundError:
    from normatrix.normatrix.source.config import LIBC_BANNED_FUNC
    from normatrix.normatrix.source.config import BAD_FILE_EXTENSION
    from normatrix.normatrix.source.config import OPERATOR_LIST

import json

class Context:
    def __init__(self, conf_path: str, only_error: str, output_format: str):
        self.LIBC_BANNED_FUNC = LIBC_BANNED_FUNC
        self.BAD_FILE_EXTENSION = BAD_FILE_EXTENSION
        self.OPERATOR_LIST = OPERATOR_LIST
        self.ENABLE_PREVIEW = False
        self.only_error = True if only_error == 'yes' else False
        if conf_path != None:
            self.set_from_file(conf_path)
        self.output_format = output_format
        if output_format in ["html", "md"]:
            self.output_file = "normatrix-result.md"
            file = open(self.output_file, "w")
            file.close()

    def set_from_file(self, path):
        try:
            with open(path, "r") as file:
                data = json.load(file)
        except Exception as e:
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
