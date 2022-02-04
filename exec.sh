#!/bin/bash

ALL_ARGS=$@

PY_MAIN_PATH=$(dirname "$0")

$PY_MAIN_PATH/main.py $ALL_ARGS
