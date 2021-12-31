#!/bin/bash
HAS_ERROR=0
grep -e " \{1,\}" -e ".* " -e $'\t\{1,\}' -e $'.*\t' -x -H -n -I $1 \
	&& HAS_ERROR=1
exit $HAS_ERROR
