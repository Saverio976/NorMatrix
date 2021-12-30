#!/bin/bash
grep -e "\n\n$$" -e "\n\n\n" -H -n -I $1 && exit 1 || exit  0
