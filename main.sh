#!/usr/bin/bash
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
echo "number of useless file : `NorMatrix/src/useless_file.sh $PWD | wc -l`"
echo "check no more than 80 char"
NorMatrix/src/count_columns.sh $PWD
echo "number of lines > 80 char : `NorMatrix/src/count_columns.sh $PWD | wc -l`"
echo "check libc function"
NorMatrix/src/libc_function.sh $PWD
echo "number of lines with libc functions : `NorMatrix/src/libc_function.sh $PWD | wc -l`"
echo "check tariling space"
NorMatrix/src/trailing_space.sh $PWD
echo "number of trailing_space : `NorMatrix/src/trailing_space.sh $PWD | wc -l`"
echo "check trailing new line"
NorMatrix/src/trailing_newline.sh $PWD
echo "number of trailing newline : `NorMatrix/src/trailing_newline.sh $PWD | wc -l`"


exit 0
