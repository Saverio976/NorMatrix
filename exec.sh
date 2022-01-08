#!/bin/bash

if [[ "$1" == "" ]]; then
	python3 $(dirname "$0")/main.py
	exit $?
fi

if [[ "$1" != "tests_run" ]]; then
	echo "USAGE:"
	echo "\t$0 [tests_run]"
	echo "DESCRIPTION:"
	echo "\tcheck norm!"
	echo "ARGS:"
	echo "\tNO ARGS:\tcheck the norm in your current working directory"
	echo "\ttests_run:\ttests the norm checker"
	exit 0
fi

cd $(dirname "$0")

python3 main.py tests_run
