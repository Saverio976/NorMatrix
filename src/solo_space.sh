#!/bin/bash
HAS_ERROR=0
NB_ERROR=`grep -e " \{1,\}" -e ".* " -e $'\t\{1,\}' -e $'.*\t' -x -I $1 -c`

if [[ $NB_ERROR == 0 ]]; then
	exit 0
else
	grep -e " \{1,\}" -e ".* " -e $'\t\{1,\}' -e $'.*\t' -x -H -n -I $1
	exit $(($NB_ERROR+0))
fi
