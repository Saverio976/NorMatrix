#!/bin/bash
grep -e "\(.*;\)\{2,\}" -H -n $1 > .tmp.txt
grep -v -e 'for' .tmp.txt > .tmp.tmp.txt

NB_ERROR=`cat .tmp.tmp.txt | wc -l`
if [[ $NB_ERROR == 0 ]]; then
	rm .tmp.txt .tmp.tmp.txt
	exit 0
else
	cat .tmp.tmp.txt
	rm .tmp.txt .tmp.tmp.txt
	exit $((NB_ERROR+0))
fi
