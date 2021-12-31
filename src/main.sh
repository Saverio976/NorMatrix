#!/bin/bash
## first argument : files to check
## seconds argument : checkers file

# COLOUR
RED='\033[0;31m'
CYAN='\033[0;36m'
GREEN='\033[0;32m'
RESET='\033[0m'

FILE_HAS_ERROR=0
HAS_ERROR=0

function process_file () {
	FILE_HAS_ERROR=0
	for CHECKER in $1; do
		./$CHECKER $FILE
		if [[ $? != 0 ]]; then
			echo -e $RED failed : $CHECKER $RESET
			FILE_HAS_ERROR=$(($FILE_HAS_ERROR+1))
		fi
	done
}

for FILE in $1; do
	if [[ $FILE == *NorMatrix* ]]; then
		continue
	fi
	if [[ $FILE == *.c || $FILE == *.h ]]; then
		echo -e $CYAN file : $FILE $RESET
		process_file "$2"
		if [[ $FILE_HAS_ERROR != 0 ]]; then
			echo -e $RED $FILE has $FILE_HAS_ERROR error.s $RESET
		else
			echo -e $GREEN ok : $FILE $RESET
		fi
		HAS_ERROR=$(($HAS_ERROR+$FILE_HAS_ERROR))
	fi
done

exit $HAS_ERROR
