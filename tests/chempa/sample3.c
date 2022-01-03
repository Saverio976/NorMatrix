/*
** EPITECH PROJECT, 2021
** divandmod
** File description:
** divmod
*/

char* res(char* str)
{
    char* left;
    char* right;
    int i = 0;
    int j = 0;
    int opr = -1;
    
    left = malloc(my_strlen(str));
    right = malloc(my_strlen(str));
    if (isadd(str, i) == 1) {
	    while (isadd(str, i) == 1) {
                left[j] = str[i];
      	        i++;
	        j++;
            }
        }
    if (isnbr(str, i) == 1) {
        while (isnbr(str, i) == 1) {
            left[j] = str[i];
            i++;
            j++;
        }
    }
    j = 0;
    while (str[i] != '\0')
    {
        opr = (opr1(str, i));
        if (opr1(str, i) != 0)
            i++;
        if (isadd(str, i) == 1) {
            while (isadd(str, i) == 1) {
                right[j] = str[i];
                j++;
                i++;
            }
        }
        if (isnbr(str, i) == 1) {
            while (isnbr(str, i) == 1) {
                right[j] = str[i];
                j++;
                i++;
            }
        }
        if (opr == 0)
            left = isneg(left, right);
        if (opr == 3)
            left = infin_mult(left, right);
        j = 0;
        right[0] = '\0';
    }
    my_putstr(left);
}

int isnbr(char* str, int i)
{
    if (str[i] == '1' | str[i] == '2' | str[i] == '3' | str[i] == '4' | str[i] == '5'
        | str[i] == '6' | str[i] == '7' | str[i] == '8' | str[i] == '9')
        return (1);
}

int isadd(char* str, int i)
{
    if (str[i] == '+' | str[i] == '-')
        return (1);
}

int ismult(char* str, int i)
{
    if (str[i] == '%' | str[i] == '/' | str[i] == '*')
        return (1);
}

int opr1(char *str, int i)
{
    if (str[i] == '+') {
        return (0);
    }
    if (str[i] == '-') {
        return (0);
    }
    if (str[i] == '/') {
	return (2);
    }
    if (str [i] == '*') {
        return (3);
    }
    if (str[i] == '%') {
        return (4);
    }
}
