##
## EPITECH PROJECT, 2021
## NorMatrix
## File description:
## the main Makefile that gather all scripts
##

# To use a custom path, call this makefile like this :
# make -C path/to/this/folder/ PATH_CHECK=path_to/check
ifndef PATH_CHECK
PATH_CHECK	=	..
endif

ifndef CHECKERS
CHECKERS	=	$(shell find src/ \( -type f \! -name main.sh -executable \))
endif

MAIN		=	src/main.sh

VPATH		=	$(MAIN) $(CHECKERS) $(FILES_TO_CHECK)

# ----------------------------------------------------------------------------

all:	up
	@echo checkers : $(notdir $(CHECKERS))
	@./$(MAIN) '$(PATH_CHECK)' '$(CHECKERS)' && \
		echo OK BRO && exit 0 || \
		echo "DUMB BRO ($(PATH_CHECK))" && exit 1

update:
	@git fetch || echo not a git repository, please uodate yourself && exit 1
	@git pull

up:
	@git pull || exit 0

tests_run:
	./tests/fn_tests/fn_tests.sh
