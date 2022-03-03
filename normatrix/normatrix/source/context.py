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
    def __init__(self, conf_path):
        self.LIBC_BANNED_FUNC = LIBC_BANNED_FUNC
        self.BAD_FILE_EXTENSION = BAD_FILE_EXTENSION
        self.OPERATOR_LIST = OPERATOR_LIST
        self.ENABLE_PREVIEW = False
        if conf_path != None:
            self.set_from_file(conf_path)

    def set_from_file(self, path):
        try:
            with open(path, "r") as file:
                data = json.load(file)
        except Exception as e:
            return None
        ret = data.get("banned", None)
        if ret != None:
            for elem in ret:
                self.LIBC_BANNED_FUNC.append(elem)
        ret = data.get("no-banned", None)
        if ret != None:
            for elem in ret:
                self.LIBC_BANNED_FUNC.remove(elem)
        ret = data.get("no-extension", None)
        if ret != None:
            for elem in ret:
                self.BAD_FILE_EXTENSION.append(elem)
        ret = data.get("enable-preview", None)
        if ret != None:
            self.ENABLE_PREVIEW = bool(ret)
