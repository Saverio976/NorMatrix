import unittest

try:
    from normatrix.test.unittests.header.tests import TestHeader
    from normatrix.test.unittests.function_line.tests import TestFunctionLine
    from normatrix.test.unittests.columns.tests import TestColumns
    from normatrix.test.unittests.comma.tests import TestComma
    from normatrix.test.unittests.indent.tests import TestIndent
    from normatrix.test.unittests.libc_func.tests import TestLibCFunc
    from normatrix.test.unittests.nb_params.tests import TestNbParams
    from normatrix.test.unittests.nested_branches.tests import TestNestedBranches
    from normatrix.test.unittests.newline_at_end_of_file.tests import TestNewlineAtEndOfFile
    from normatrix.test.unittests.number_function.tests import TestNumberFunction
    from normatrix.test.unittests.operators.tests import TestOperators
    from normatrix.test.unittests.parenthesis.tests import TestParenthesis
    from normatrix.test.unittests.preprocessor.tests import TestPreprocessor
    from normatrix.test.unittests.snake_case.tests import TestSnakeCase
    from normatrix.test.unittests.solo_space.tests import TestSoloSpace
    from normatrix.test.unittests.statements.tests import TestStatements
    from normatrix.test.unittests.trailing_newline.tests import TestTrailingNewline
    from normatrix.test.unittests.two_space.tests import TestTwoSpace
    exe = "normatrix.test.tests"
except ModuleNotFoundError:
    from src.normatrix.test.unittests.header.tests import TestHeader
    from src.normatrix.test.unittests.function_line.tests import TestFunctionLine
    from src.normatrix.test.unittests.columns.tests import TestColumns
    from src.normatrix.test.unittests.comma.tests import TestComma
    from src.normatrix.test.unittests.indent.tests import TestIndent
    from src.normatrix.test.unittests.libc_func.tests import TestLibCFunc
    from src.normatrix.test.unittests.nb_params.tests import TestNbParams
    from src.normatrix.test.unittests.nested_branches.tests import TestNestedBranches
    from src.normatrix.test.unittests.newline_at_end_of_file.tests import TestNewlineAtEndOfFile
    from src.normatrix.test.unittests.number_function.tests import TestNumberFunction
    from src.normatrix.test.unittests.operators.tests import TestOperators
    from src.normatrix.test.unittests.parenthesis.tests import TestParenthesis
    from src.normatrix.test.unittests.preprocessor.tests import TestPreprocessor
    from src.normatrix.test.unittests.snake_case.tests import TestSnakeCase
    from src.normatrix.test.unittests.solo_space.tests import TestSoloSpace
    from src.normatrix.test.unittests.statements.tests import TestStatements
    from src.normatrix.test.unittests.trailing_newline.tests import TestTrailingNewline
    from src.normatrix.test.unittests.two_space.tests import TestTwoSpace
    exe = "src.normatrix.test.tests"

import subprocess

def run_tests():
    ret = subprocess.run(["python3", "-m", "unittest", exe, "-v"])
    return ret.returncode

if __name__ == "__main__":
    unittest.main()
