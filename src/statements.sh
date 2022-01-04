#!/bin/bash
TMP=.tmp.txt
TMPTMP=.tmp.tmp.txt

grep -e "\(.*;\)\{2,\}" -H -n $1 > $TMP
grep -v -e 'for' $TMP > $TMPTMP

NB_ERROR=`cat $TMPTMP | wc -l`
if [[ $NB_ERROR == 0 ]]; then
	rm $TMP $TMPTMP
	exit 0
else
	cat $TMPTMP
	rm $TMP $TMPTMP
	exit $((NB_ERROR+0))
fi
