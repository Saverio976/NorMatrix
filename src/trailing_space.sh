#!/usr/bin/env sh
##
## EPITECH PROJECT, 2021
## NorMatrix
## File description:
## check if there are tariling space
##

grep -e " " -x -H -n -r -I --exclude-dir=tests --exclude-dir=.git \
        --exclude-dir=.github --exclude-dir=NorMatrix $1
exit 0
