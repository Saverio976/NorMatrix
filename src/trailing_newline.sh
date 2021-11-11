#!/usr/bin/env sh
##
## EPITECH PROJECT, 2021
## NorMatrix
## File description:
## check if there are tariling newline
##

grep -e "\n\n$" -H -n -r -I --exclude-dir=tests --exclude-dir=.git \
        --exclude-dir=.github --exclude-dir=NorMatrix $1
exit 0
