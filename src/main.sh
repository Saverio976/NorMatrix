#!/bin/bash
## first argument : files to check
## seconds argument : checkers file

# COLOUR
RED='\033[0;31m'
BOLDRED='\033[1;31m'
CYAN='\033[0;36m'
GREEN='\033[0;32m'
RESET='\033[0m'


FILES_TO_CHECK=`find $1 -type f`
CURRENT_INDEX=1
MAX_INDEX=0

FILE_HAS_ERROR=0
HAS_ERROR=0
LAST=0

function process_file () {
	FILE_HAS_ERROR=0
	for CHECKER in $1; do
		./$CHECKER $FILE
		LAST=$(($?+0))
		FILE_HAS_ERROR=$(($FILE_HAS_ERROR+$LAST))
		if [[ $LAST != 0 ]]; then
			echo -e $RED failed : $CHECKER $RESET
		fi
	done
}

for FILE in $FILES_TO_CHECK; do
	if [[ $FILE == *NorMatrix* || $FILE == *.git/* ]]; then
		continue
	fi
	if [[ $FILE == *.o || $FILE == *.a || $FILE == *.gcno || $FILE == *.gcda ]]; then
		continue
	fi
	if [[ $FILE == *.c || $FILE == *.h ]]; then
		MAX_INDEX=$(($MAX_INDEX+1))
	fi
done

for FILE in $FILES_TO_CHECK; do
	if [[ $FILE == *NorMatrix* || $FILE == *.git/* ]]; then
		continue
	fi
	if [[ $FILE == *.o || $FILE == *.a || $FILE == *.gcno || $FILE == *.gcda ]]; then
		echo -e $RED WTF file : $FILE $RESET
		HAS_ERROR=$(($HAS_ERROR+1))
		continue
	fi
	if [[ $FILE == *.c || $FILE == *.h ]]; then
		process_file "$2"
		if [[ $FILE_HAS_ERROR != 0 ]]; then
			echo -e $BOLDRED -\> nope : $FILE : $FILE_HAS_ERROR err $RESET
		else
			echo -e $GREEN -\> ok : $FILE $RESET
		fi
		HAS_ERROR=$(($HAS_ERROR+$FILE_HAS_ERROR))
		echo -e $CYAN ..[file n° $CURRENT_INDEX / $MAX_INDEX] $RESET
		CURRENT_INDEX=$(($CURRENT_INDEX+1))
	fi
done

if [[ $HAS_ERROR == 0 ]]; then
	echo -e $GREEN [✓] You Have No Error GG Bro $RESET
	exit 0
else
	echo -e $BOLDRED [x] You Have $HAS_ERROR error.s $RESET
	exit 1
fi
