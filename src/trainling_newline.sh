#!/bin/bash
HAS_ERROR=0
RES=`cat $1 -e`
echo $RES | grep -e "$ $ $ " -q && HAS_ERROR=1
if [[ $HAS_ERROR == 1 ]]; then
	echo $1: only 1 newline between function
fi
if [[ `tail $1 -n 1 | cat -e` == "$" ]]; then
	echo $1: only 1 newline at the end of file
	HAS_ERROR=1
fi
exit $HAS_ERROR
