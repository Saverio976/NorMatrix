#!/bin/bash
grep -e " " -x -H -n -I $1 && exit 1 || exit 0
