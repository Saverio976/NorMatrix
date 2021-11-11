#!/usr/bin/env sh
##
## EPITECH PROJECT, 2021
## NorMatrix
## File description:
## check if there are libc function call
##

grep -e "printf" -w -H -n -r -I --exclude-dir=tests --exclude-dir=.git \
        --exclude-dir=.github --exclude-dir=NorMatrix $1
grep -e "strlen" -w -H -n -r -I --exclude-dir=tests --exclude-dir=.git \
        --exclude-dir=.github --exclude-dir=NorMatrix $1

exit 0
