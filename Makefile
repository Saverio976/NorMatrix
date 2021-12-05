##
## EPITECH PROJECT, 2021
## NorMatrix
## File description:
## the main Makefile that gather all scripts
##

# COLOUR
CYAN		=	'\033[0;36m'
GREEN		=	'\033[0;32m'
RESET		=	'\033[0m'

# To use a custom path, call this makefile like this :
# make -C path/to/this/folder/ PATH_CHECK=path_to/check
PATH_CHECK	?=	..

# Add some function that are forbiden to thsi list
LIBC_FUNC	=	-e 'printf(' -e 'memset(' \
			-e 'calloc(' -e 'strcpy(' \
			-e 'strcat('

# ----------------------------------------------------------------------------

all: columns libc_func trling_newline solo_space two_space usls_file

columns:
	@    echo -e $(CYAN)check colums:$(RESET)
	@grep -e ".\{80,\}" -H -n -r -I --exclude-dir=tests \
	  --exclude-dir=.git --exclude-dir=.github \
	  --exclude-dir=NorMatrix $(PATH_CHECK) && exit 1 || \
	  echo -e $(GREEN)no columns more than 80 char$(RESET)

libc_func:
	@    echo -e $(CYAN)check libc func:$(RESET)
	@grep $(LIBC_FUNC) -w -H -n -r -I --exclude-dir=tests \
	  --exclude-dir=.git --exclude-dir=.github \
	  --exclude-dir=NorMatrix $(PATH_CHECK) && exit 1 || \
	  echo -e $(GREEN)no libc functions$(RESET)

trling_newline:
	@    echo -e $(CYAN)check trailing new line:$(RESET)
	@grep -e "\n\n$$" -e "\n\n\n" -H -n -r -I --exclude-dir=tests \
	  --exclude-dir=.git --exclude-dir=.github \
	  --exclude-dir=NorMatrix $(PATH_CHECK) && exit 1 || \
	  echo -e $(GREEN)no trailing new line$(RESET)

solo_space:
	@    echo -e $(CYAN)check solo space on line:$(RESET)
	@grep -e " " -x -H -n -r -I --exclude-dir=tests \
	  --exclude-dir=.git --exclude-dir=.github \
	  -exclude-dir=NorMatrix $(PATH_CHECK) && exit 1 || \
	  echo -e $(GREEN)no space solo$(RESET)

two_space:
	@echo -e $(CYAN)two space next each other:$(RESET)
	@grep -e '.*[a-zA-Z0-9]  .*' -x -H -n -r -I --exclude-dir=tests \
	  --exclude-dir=.git --exclude-dir=.github \
	  -exclude=NorMatrix --exclude=Makefile $(PATH_CHECK) && exit 1 || \
	  echo -e $(GREEN)no two space$(RESET)

usls_file:
	@echo -e $(CYAN)useless file:$(RESET)
	@find $(PATH_CHECK) -type f -a \( -name '*.o' -o -name '*.gc' \
	  -o -name '*.a' -o -name '*.so' -o -name '*~' -o -name '*.d' \) | \
	  grep . && exit 1 || \
	  echo -e $(GREEN)no useless file$(RESET)
