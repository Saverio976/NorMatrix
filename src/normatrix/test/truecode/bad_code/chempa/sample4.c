/*
** EPITECH PROJECT, 2021
** infinite add
** File description:
** infini add
*/
#include "include/my.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char *asciiadd(char *left, char *result, int i, int ret)
{
    int k = 0;

    while (left[i] != '\0') {
        result[i] = (left[i] - '0') + ret;
        if (result[i] >= 10)
            ret = result[i] / 10, result[i] %= 10;
        else
            ret = 0;
        i++;
    }
    if (ret > 0) {
        result[i] = ret;
        i++;
    }
    while (k != i) {
        result[k] += '0';
        k++;
    }
    result = my_revstr(result);
    return (result);
}

char *infin_add(char *left, char *right)
{
    char *result = 0, *temp;
    int i = 0, ret = 0;
    temp = malloc(1000), temp = my_strcpy(temp, left);
    if (my_strlen(left) < my_strlen(right)) {
        left = my_strcpy(left, right);
        right = malloc(sizeof(char) * strlen(left) + 1);
        right = my_strcpy(right, temp);
    }
    result = malloc(sizeof(char) * (strlen(left) + strlen(right) + 2));
    left = my_revstr(left), right = my_revstr(right);
    while (i != my_strlen(right)) {
        result[i] = ((left[i] - '0') + (right[i] - '0')) + ret;
        if (result[i] >= 10)
            ret = result[i] / 10, result[i] %= 10;
        else
            ret = 0;
        i++;
    }
    result = asciiadd(left, result, i, ret);
    return (result);
}

