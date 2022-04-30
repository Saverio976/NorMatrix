import unittest

try:
    from normatrix.test.header.tests import TestHeader
    from normatrix.test.function_line.tests import TestFunctionLine
    from normatrix.test.columns.tests import TestColumns
    from normatrix.test.comma.tests import TestComma
    from normatrix.test.indent.tests import TestIndent
    from normatrix.test.libc_func.tests import TestLibCFunc
    from normatrix.test.nb_params.tests import TestNbParams
    from normatrix.test.nested_branches.tests import TestNestedBranches
    from normatrix.test.newline_at_end_of_file.tests import TestNewlineAtEndOfFile
    from normatrix.test.number_function.tests import TestNumberFunction
    from normatrix.test.operators.tests import TestOperators
    from normatrix.test.parenthesis.tests import TestParenthesis
    from normatrix.test.preprocessor.tests import TestPreprocessor
    from normatrix.test.snake_case.tests import TestSnakeCase
    from normatrix.test.solo_space.tests import TestSoloSpace
    from normatrix.test.statements.tests import TestStatements
    from normatrix.test.trailing_newline.tests import TestTrailingNewline
    from normatrix.test.two_space.tests import TestTwoSpace
    exe = "normatrix.test.tests"
except ModuleNotFoundError:
    from src.normatrix.test.header.tests import TestHeader
    from src.normatrix.test.function_line.tests import TestFunctionLine
    from src.normatrix.test.columns.tests import TestColumns
    from src.normatrix.test.comma.tests import TestComma
    from src.normatrix.test.indent.tests import TestIndent
    from src.normatrix.test.libc_func.tests import TestLibCFunc
    from src.normatrix.test.nb_params.tests import TestNbParams
    from src.normatrix.test.nested_branches.tests import TestNestedBranches
    from src.normatrix.test.newline_at_end_of_file.tests import TestNewlineAtEndOfFile
    from src.normatrix.test.number_function.tests import TestNumberFunction
    from src.normatrix.test.operators.tests import TestOperators
    from src.normatrix.test.parenthesis.tests import TestParenthesis
    from src.normatrix.test.preprocessor.tests import TestPreprocessor
    from src.normatrix.test.snake_case.tests import TestSnakeCase
    from src.normatrix.test.solo_space.tests import TestSoloSpace
    from src.normatrix.test.statements.tests import TestStatements
    from src.normatrix.test.trailing_newline.tests import TestTrailingNewline
    from src.normatrix.test.two_space.tests import TestTwoSpace
    exe = "src.normatrix.test.tests"

import subprocess

def run_tests():
    subprocess.call(["python3", "-m", "unittest", exe, "-v"])

if __name__ == "__main__":
    unittest.main()
