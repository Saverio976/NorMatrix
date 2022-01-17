/*
** EPITECH PROJECT, 2021
** infin mult
** File description:
** infinmult
*/
#include "include/my.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char* infin_mult(char* l, char* r)
{
    char* result = NULL;
    char* left;
    char* right;
    int i = 0;
    int ret = 0;
    int left_neg = 0;
    int right_neg = 0;
    int j = 0;

    left = malloc(my_strlen(l));
    right = malloc(my_strlen(r));
    
    while (l[j] == '-' || l[j] == '+') {
        if (l[j] == '-')
            left_neg += 1;
        j++;
    }
    j = 0;
    while (r[j] == '-' || r[j] == '+') {
        if (r[j] == '-')
            right_neg += 1;
        j++;
    }
    j = 0;
    while (l[i] != '\0') {
        if (l[i] != '-' && l[i] != '+') {
            left[j] = l[i];
            j++;
        }
        i++;
    }
    j = 0;
    i = 0;
    while (r[i] != '\0') {
        if (r[i] != '-' && r[i] != '+') {
            right[j] = r[i];
            j++;
        }
        i++;
    }
    result = malloc(sizeof(char) * (my_strlen(left) + my_strlen(right) + 1));
    left = my_revstr(left);
    right = my_revstr(right);
    for (int i1 = 0; left[i1] != '\0'; i1++) {
        i = i1;
        for (int i2 = 0; right[i2] != '\0'; i2++) {
            result[i] += (left[i1] - '0') * (right[i2] - '0') + ret;
            if (result[i] >= 10) {
                ret = result[i] / 10;
                result[i] %= 10;
            } else {
                ret = 0;
            }
            i++;
        }
    }
    if (ret > 0) {
        result[i] = ret;
        i++;
    }
    for (int j = 0; j < i; j++) {
        result[j] += '0';
    }
    if ((left_neg + right_neg) % 2 != 0) {
        result[i] = '-';
        i++;
    }
    result = my_revstr(result);
    return result;
}
