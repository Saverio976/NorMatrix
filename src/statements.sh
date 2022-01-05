#!/bin/bash
TMP=.tmp.txt
TMPTMP=.tmp.tmp.txt

cat $1 > $TMP
sed '/\/\*/,/\*\//d' $TMP > $TMPTMP
cat $TMPTMP > $TMP

grep -e "\(.*;\)\{2,\}" -H -n $TMP > $TMPTMP
grep -v -e 'for' $TMPTMP > $TMP
grep -v -e '".*;.*"' $TMP > $TMPTMP
grep -v -e '//.*;.*"' $TMPTMP > $TMP

NB_ERROR=`cat $TMP | wc -l`
if [[ $NB_ERROR == 0 ]]; then
	rm $TMP $TMPTMP
	exit 0
else
	cat $TMP
	rm $TMP $TMPTMP
	exit $((NB_ERROR+0))
fi
