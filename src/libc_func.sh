#!/bin/bash
LIBC_FUNC="-e 'printf(' -e 'memset(' -e 'calloc(' -e 'strcpy(' -e 'strcat('"
NB_ERROR=`grep $LIBC_FUNC -w -I $1 -c`

if [[ $NB_ERROR == 0 ]]; then
	exit 0
else
	grep $LIBC_FUNC -w -H -n -I $1
	exit $(($NB_ERROR+0))
fi
