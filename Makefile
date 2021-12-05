##
## EPITECH PROJECT, 2021
## NorMatrix
## File description:
## the main Makefile that gather all scripts
##

# To use a custom path, call this makefile like this :
# make -C path/to/this/folder/ PATH_CHECK=path_to/check
PATH_CHECK	?=	..

# Add some function that are forbiden to thsi list
LIBC_FUNC	=	-e 'printf(' -e 'memset(' \
			-e 'calloc(' -e 'strcpy(' \
			-e 'strcat('

# ----------------------------------------------------------------------------

all: columns libc_func trling_newline solo_space two_space

columns:
	@grep -e ".\{81,\}" -H -n -r -I --exclude-dir=tests \
	  --exclude-dir=.git --exclude-dir=.github \
	  --exclude-dir=NorMatrix $(PATH_CHECK) || \
	  echo "no columns more than 80 char"

libc_func:
	@grep $(LIBC_FUNC) -w -H -n -r -I --exclude-dir=tests \
	  --exclude-dir=.git --exclude-dir=.github \
	  --exclude-dir=NorMatrix $(PATH_CHECK) || \
	  echo "no libc functions"

trling_newline:
	@grep -e "\n\n$$" -e "\n\n\n" -H -n -r -I --exclude-dir=tests \
	  --exclude-dir=.git --exclude-dir=.github \
	  --exclude-dir=NorMatrix $(PATH_CHECK) || \
	  echo "no trailing new line"

solo_space:
	@grep -e " " -x -H -n -r -I --exclude-dir=tests \
	  --exclude-dir=.git --exclude-dir=.github \
	  -exclude-dir=NorMatrix $(PATH_CHECK) || \
	  echo "no space solo"

two_space:
	@grep -e '.*[a-zA-Z0-9]  .*' -x -H -n -r -I --exclude-dir=tests \
	  --exclude-dir=.git --exclude-dir=.github \
	  -exclude=NorMatrix --exclude=Makefile $(PATH_CHECK) || \
	  echo "no two space"
