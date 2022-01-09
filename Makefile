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

fclean:
	rm -rf dist/*

build: fclean build-test build-prod

build-test:
	echo ON TEST NORMATRIX
	python3 -m pip install --upgrade build
	python3 -m build
	python3 -m pip install --upgrade twine
	python3 -m twine upload --repository testpypi dist/* --verbose

build-prod:
	echo ON NORMATRIX
	python3 -m build
	python3 -m twine upload dist/*
