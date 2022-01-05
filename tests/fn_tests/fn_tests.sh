#!/bin/bash
function assert_err_code () {
	if [[ $1 == 0 ]]; then
		exit 1
	fi
}

function assert_ok_code () {
	if [[ $1 != 0 ]]; then
		exit 1
	fi
}

echo columns
./src/columns.sh tests/bad_code/line_81_chars.c
assert_err_code $?
./src/columns.sh tests/ok_code/line_80_chars.c
assert_ok_code $?
echo comma
./src/comma.sh tests/bad_code/comma.c
assert_err_code $?
./src/comma.sh tests/ok_code/comma.c
assert_ok_code $?
echo function_line
./src/function_line.py tests/bad_code/chempa/sample1.c
assert_err_code $?
./src/function_line.py tests/ok_code/20_line_func.c
assert_ok_code $?
