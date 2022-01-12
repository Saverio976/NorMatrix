#!/bin/bash

LAST_PWD=$PWD
ALL_ARGS=$@

cd $(dirname "$0")

if [[ "$ALL_ARGS" == "" ]]; then
	python3 main.py $LAST_PWD
else
	python3 main.py $ALL_ARGS
fi
