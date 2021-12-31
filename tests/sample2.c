/*
** EPITECH PROJECT, 2021
** base
** File description:
** create the base for bistro-matic
*/

#include <stdlib.h>
#include "../lib/my/my.h"

char *base(char *calc, char *bnb, char *bop)
{
    char *result;
    char nb[] = "0123456789";
    char op[] = "()+-*/%";
    char temp = op[0];
    int tempindex = 0;
    int resindex = 0;

    result = malloc(sizeof(char) * my_strlen(calc) + 1);
    for (int i = 0; calc[i] != '\0'; i++) {
        for (int j = 0; bnb[j] != '\0'; j++) {
            if (bnb[j] == calc[i]) {
                op[tempindex] = temp;
                result[resindex] = nb[j];
                resindex++;
            } else {
                for (int k = 1; bop[k] != '\0'; k++) {
                    if (bop[k] == calc[i]) {
                        result[resindex] = op[k];
                        resindex++;
                        temp = bop[k];
                        tempindex = k;
                        bop[k] = bop[k+1];
                    }
                }
            }
        }
    }
    result[resindex] = '\0';
    return result;
    free(result);
}

char *resbase(char *res, char *bnb)
{
    char *result;
    char nb[] = "0123456789";
    int resindex = 0;

    result = malloc(sizeof(char) * my_strlen(res) + 1);
    for (int i = 0; res[i] != '\0'; i++) {
        for (int j = 0; nb[j] != '\0'; j++) {
            if (res[i] == nb[j]) {
                result[resindex] = bnb[j];
                resindex++;
            }
        }
    }
    result[resindex] = '\0';
    return result;
    free(result);
}
