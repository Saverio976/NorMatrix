#!/bin/bash
grep -e '.*[a-zA-Z0-9]  .*' -x -H -n -I $1 && exit 1 || exit 0
