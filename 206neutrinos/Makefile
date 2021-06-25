##
## EPITECH PROJECT, 2019
## Makefile
## File description:
## make
##

NAME    =	206neutrinos

SRC     =	206neutrinos.py

all:	$(NAME)

$(NAME):
	cp $(SRC) $(NAME)
	chmod +x $(NAME)

clean:

fclean: clean
	rm -f $(NAME)

re: fclean all

tests_run:
	rm -f *.gcda
	rm -f *.gcno

tests_clean:
	rm -f *.gcda
	rm -f *.gcno
