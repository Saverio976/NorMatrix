#!/bin/bash
NB_ERROR=`grep ".\{81,\}" $1 -c`

if [[ $NB_ERROR == 0 ]]; then
	exit 0
else
	grep -e ".\{81,\}" -H -n -I $1
	exit $(($NB_ERROR+0))
fi
