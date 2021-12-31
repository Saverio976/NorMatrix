#!/bin/bash
RES=`cat $1 -e`
NB_ERROR_ONE=`echo $RES | grep -e "$ $ $ " -c`

if [[ $NB_ERROR_ONE != 0 ]]; then
	echo $1: only 1 newline between function \($NB_ERROR_ONE error\)
fi
if [[ `tail $1 -n 1 | cat -e` == "$" ]]; then
	echo $1: only 1 newline at the end of file
	NB_ERROR_ONE=$((NB_ERROR_ONE+1))
fi
exit $NB_ERROR_ONE
