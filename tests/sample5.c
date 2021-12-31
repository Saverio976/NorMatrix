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

char *asciiadd2(char *left, char *result, int i, int ret)
{
    int k = 0;
    while (left[i] != '\0') {
        result[i] = left[i] - '0' + ret;
        ret = 0;
        if (result[i] < 0) {
            result[i] += 10;
            ret = - 1;
        } else {
            ret = 0;
        }
        i++;
    }
    while (k != i) {
        result[k] += '0';
        k++;
    }
    return (result);
}

char *infin_minus(char *left, char *right)
{
    char *result = 0, *temp;
    int i = 0, ret = 0, stock = 5;
    int left_neg = 0, right_neg = 0;
    temp = malloc(1000), temp = my_strcpy(temp, left);
    result = malloc(sizeof(char) * (strlen(left) + strlen(right) + 100));
    if (my_strlen(left) < my_strlen(right)) {
        left = my_strcpy(left, right);
        right = malloc(sizeof(char) * strlen(left) + 1);
        right = my_strcpy(right, temp);
    }
    if (my_strlen(left) == my_strlen(right)) {
        if (left[0] < right[0]) {
            left = my_strcpy(left, right);
            right = malloc(sizeof(char) * strlen(left) + 1);
            right = my_strcpy(right, temp);
        }
    }
    left = my_revstr(left), right = my_revstr(right);
    while (i != my_strlen(right)) {
        result[i] = ((left[i] - '0') - (right[i] - '0')) + ret;
        if (result[i] < 0)
            result[i] = result[i] + 10, ret = -1;
        else
            ret = 0;
        i++;
    }
    result = asciiadd2(left, result, i, ret);
    result = my_revstr(result);
    return (result);
}
