#!/usr/bin/env sh
##
## EPITECH PROJECT, 2021
## NorMatrix
## File description:
## check on each lines of files found if > 80
##

grep -e ".\{80,\}" -H -n -r -I --exclude-dir=tests $1
