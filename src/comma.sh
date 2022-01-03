#!/bin/bash
NB_ERROR=`grep -e ',\S' -I $1 -c`

if [[ $NB_ERROR == 0 ]]; then
	exit 0
else
	grep -e ',\S' -H -n -I $1
	exit $(($NB_ERROR+0))
fi
