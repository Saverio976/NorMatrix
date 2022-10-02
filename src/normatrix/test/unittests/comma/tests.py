import unittest
import tempfile

try:
    from normatrix.source.file_parser import parse
    from normatrix.plugged.comma import check
    from normatrix.source.context import Context
except ModuleNotFoundError:
    from src.normatrix.source.file_parser import parse
    from src.normatrix.plugged.comma import check
    from src.normatrix.source.context import Context

ok_code = """
int func(int c, int d)
{
    return c + d;
}

int func2(int h)
{
    return func(h, h);
}

// a,b
/*
** a,b
*/

int func3(int a)
{
    func(func(a, a), func(a, a));
    return a;
}"""

bad_code = """
int bfunc(int c ,int d)
{
    return c + d;
}

int func(int h)
{
    return bfunc(h,h);
}

int foo(int a)
{
    for (int i = 0 ,e = a; i < e; i++);
    return a;
}"""

class TestComma(unittest.TestCase):

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
        self.assertEqual(list_error[0][0], 2)
        self.assertEqual(list_error[1][0], 9)
        self.assertEqual(list_error[2][0], 14)