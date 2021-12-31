/*
** EPITECH PROJECT, 2021
** main
** File description:
** main
*/

#include <stdlib.h>
#include <stdio.h>
#include "include/my.h"

char *isneg(char *l, char *r)
{
    char* right;
    char* left;
    int left_neg = 0;
    int right_neg = 0;
    int neg = 0;
    char* result;
    char* final;
    int i = 0, j = 0, k = 0, m = 0;
    int stock;

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
    neg += left_neg + right_neg;
    stock = who_is_higher(left, right, left_neg, right_neg);
    if (neg % 2 == 0)
        result = infin_add(left, right);
    else {
        result = infin_minus(left, right);
    }
    if (op(neg) == 1) {
        my_revstr(result);
        if (stock == 0)
            result[my_strlen(result)] = '-';
        if (stock == 1 && left_neg % 2 == 1)
            result[my_strlen(result)] = '-';
        my_revstr(result); 
    }
    
    if (op(neg) == 0) {
        result = my_revstr(result);
        if (right_neg % 2 == 1 && left_neg % 2 == 1)	
          result[my_strlen(result)] = '-';
        else if (stock == 0 && left_neg % 2 == 1)
            result[my_strlen(result)] = '-';

        result = my_revstr(result);   
    }
    i = 0;
    j = 0;
    if (result[0] == '0')
        m = 1;
    final = malloc(my_strlen(result));
    while (i != my_strlen(result)) {
        if (result[i] == '-') {
            final[j] = result[i];
            i++;
            j++;
            k = 1;
        }
        if (m == 1 || k == 1)
           while (result[i] == '0' && i != my_strlen(result) - 1)
               i++;
        k = 0;
        m = 0;
        final[j] = result[i];
        i++;
        j++;
    }
    return (final);
}

int op(int neg)
{
    if (neg % 2 == 1)
        return (1);
    if (neg % 2 == 0)
        return (0);
    
}

int who_is_higher(char* left, char* right, int left_neg, int right_neg)
{
    int i = 0;
    int a = 0;
    int resa = 0;
    int resb = 0;
    if (left_neg % 2 != 0)
        a = 1;
    while (left[i] != '\0') {
        resa = resa * 10;
        resa += left[i] - '0';
        i++;
    }
    i = 0;
    while (right[i] != '\0') {
	resb = resb * 10;
	resb += right[i] - '0';
        i++;
    }
    if (resa > resb)
        return (1);
    else
        return (0);
}
