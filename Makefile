##
## EPITECH PROJECT, 2021
## NorMatrix
## File description:
## the main Makefile that gather all scripts
##

# To use a custom path, call this makefile like this :
# make -C path/to/this/folder/ PATH_CHECK=path_to/check
PATH_CHECK	?=	..

FILES_TO_CHECK	=	$(shell find $(PATH_CHECK) -type f)

CHECKERS	=	$(shell find src/ \( -type f \! -name main.sh \))

MAIN		=	src/main.sh

VPATH		=	$(MAIN) $(CHECKERS) $(FILES_TO_CHECK)

# ----------------------------------------------------------------------------

all:
	@echo checkers : $(notdir $(CHECKERS))
	@./$(MAIN) '$(FILES_TO_CHECK)' '$(CHECKERS)' && \
		echo OK BRO && exit 0 || \
		echo "DUMB BRO ($(PATH_CHECK))" && exit 1
