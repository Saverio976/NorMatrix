#!/usr/bin/env sh
##
## EPITECH PROJECT, 2021
## NorMatrix
## File description:
## check if there are useless file
##

find $1 -name '*.git*' -prune -o \
        \( -type f -a \
        \! -name Makefile -a \
        \! -name README.md -a \
        \! -name '*.c' -a \
        \! -name '*.h' -a \
        \! -name '*.sh' \
        -print \)
