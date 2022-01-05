#!/bin/bash
TMP=.tmp.txt
TMPTMP=.tmp.tmp.txt

cat $1 > $TMP
sed '/\/\*/,/\*\//d' $TMP > $TMPTMP
cat $TMPTMP > $TMP

for I in 0..3
do
	grep -e "\(.*;\)\{2,\}" -H -n $TMP > $TMPTMP
	grep -v -e 'for' $TMPTMP > $TMP
	grep -v -e '".*;.*"' $TMP > $TMPTMP
	grep -v -e '//.*;.*"' $TMPTMP > $TMP
done

NB_ERROR=`cat $TMPTMP | wc -l`
if [[ $NB_ERROR == 0 ]]; then
	rm $TMP $TMPTMP
	exit 0
else
	cat $TMPTMP
	rm $TMP $TMPTMP
	exit $((NB_ERROR+0))
fi
