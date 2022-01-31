#!/usr/bin/env python3
import sys

try:
    from normatrix.source.main import main
except ModuleNotFoundError:
    from normatrix.normatrix.source.main import main

if len(sys.argv) > 1 and sys.argv[1] == "--tests-run":
    from test.fn_tests import tests
    exit(tests.main())
else:
    exit(main())
