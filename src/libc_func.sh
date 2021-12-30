#!/bin/bash
##
LIBC_FUNC="-e 'printf(' -e 'memset(' -e 'calloc(' -e 'strcpy(' -e 'strcat('"
grep $LIBC_FUNC -w -H -n -I $1 && exit 1 || exit 0
