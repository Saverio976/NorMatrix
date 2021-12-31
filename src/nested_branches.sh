#!/bin/bash
HAS_ERROR=0
grep -e " \{16,\}.*" -x -H -n -I $1 && HAS_ERROR=1
exit $HAS_ERROR
