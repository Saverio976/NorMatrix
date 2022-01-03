#!/bin/bash
NB_ERROR=`grep -e "\(.*;\)\{2,\}" -I -c $1`

if [[ $NB_ERROR == 0 ]]; then
	exit 0
else
	grep -e "\(.*;\)\{2,\}" -H -n -I $1
	exit $(($NB_ERROR+0))
fi
