#!/bin/bash

make -C $(dirname "$0") PATH_CHECK="$1" -s
