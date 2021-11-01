#!/usr/bin/env sh
##
## EPITECH PROJECT, 2021
## NorMatrix
## File description:
## execute all shell script in src/
##

echo "check folder : $PWD"
echo ""
echo "check useless file :"
NorMatrix/src/useless_file.sh $PWD
echo "number of useless file : `NorMatrix/src/useless_file.sh | wc -l`"
echo "check no more than 80 char"
NorMatrix/src/count_columns.sh $PWD
echo "number of lines > 80 char : `NorMatrix/src/count_columns.sh | wc -l`"

exit 0
