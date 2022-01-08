##
## EPITECH PROJECT, 2022
## NorMatrix
## File description:
## execute the norm checker
##

ifndef PATH_CHECK
PATH_CHECK	=	..
endif

CWD		=	$(shell env | grep -e "^PWD=" | cut -d= -f2)

MAIN		=	main.py

# ----------------------------------------------------------------------------

all: $(CWD)
	cd $(PATH_CHECK) && $(CWD)/$(MAIN)

tests_run:
	./$(MAIN) tests_run
