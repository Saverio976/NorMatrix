#!/bin/bash

make -C $(dirname "$0") PATH_CHECK="$PWD" -s
