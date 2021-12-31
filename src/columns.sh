#!/bin/bash
## check if first argument contains more than 80 char on all line
## if 80 char exit 1
## else 0
grep -e ".\{81,\}" -H -n -I $1 && exit 1 || exit 0
