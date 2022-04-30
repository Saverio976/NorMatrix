import unittest
import tempfile

try:
    from normatrix.source.file_parser import parse
    from normatrix.plugged.libc_func import check
    from normatrix.source.context import Context
except ModuleNotFoundError:
    from src.normatrix.source.file_parser import parse
    from src.normatrix.plugged.libc_func import check
    from src.normatrix.source.context import Context

ok_code = """
int main()
{
    my_printf("")
}
"""

bad_code = """
int main()
{
    printf("")
}
"""

class TestLibCFunc(unittest.TestCase):

    _fd_ko = None
    _name_ko = None
    _fd_ok = None
    _name_ok = None

    def _create_files(self):
        if self._fd_ko != None:
            return
        self._fd_ok, self._name_ok = tempfile.mkstemp(
            suffix=".c",
            prefix="normatrix_test_ok_",
            text=True)
        self._fd_ko, self._name_ko = tempfile.mkstemp(
            suffix=".c",
            prefix="normatrix_test_ko_",
            text=True)
        with open(self._name_ok, "w") as fd:
            print(ok_code, file=fd)
        with open(self._name_ko, "w") as fd:
            print(bad_code, file=fd)

    def test_ok_file(self):
        self._create_files()
        parsed, nb_line = parse(self._name_ok, "")
        context = Context(path="", only_error=True, output_format="term_color")
        nb_error, hight, list_error = check(context, parsed)
        self.assertEqual(nb_error, 0)

    def test_ko_file(self):
        self._create_files()
        parsed, nb_line = parse(self._name_ko, "")
        context = Context(path="", only_error=True, output_format="term_color")
        nb_error, hight, list_error = check(context, parsed)
        self.assertNotEqual(nb_error, 0)
        self.assertEqual(list_error[0][0], 4)
