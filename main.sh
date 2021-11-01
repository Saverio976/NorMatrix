#!/usr/bin/env sh
##
## EPITECH PROJECT, 2021
## NorMatrix
## File description:
## execute all shell script in src/
##

if [[ "$1" -eq "" ]]
then
    PREFIX=$PWD
else
    PREFIX=$1
fi

echo "check folder : $PREFIX"

echo "check useless file :"
src/useless_file.sh $PREFIX
echo "number of useless file : `src/useless_file.sh | wc -l`"
echo "check no more than 80 char"
src/count_columns.sh $PREFIX
echo "number of lines > 80 char : `src/count_columns.sh | wc -l`"

exit 0
