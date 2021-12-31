#!/bin/bash
HAS_ERROR=0
grep -e " \{15,\}.*" -x -H -n -I $1 && HAS_ERROR=1
exit $HAS_ERROR
