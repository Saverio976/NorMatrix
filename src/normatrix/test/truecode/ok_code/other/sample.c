/*
** EPITECH PROJECT, 2021
** linked_list lib
** File description:
** Merges two sorted array
** Does it very poorly
*/

#include "linked_list.h"
#include <stddef.h>

int my_add_in_sorted_list(linked_list_t **, void *data, int(*cmp)(), int lol);

void my_merge(linked_list_t **begin1, linked_list_t *begin2, int(*cmp)())
{
    linked_list_t *cp;
    linked_list_t *next;

    cp = begin2;
    if (*begin1 == NULL) {
        *begin1 = begin2;
        return;

    }
    while (cp != NULL) {
        next = cp -> next;
        my_add_in_sorted_list(begin1, cp -> data, cmp);
        cp = next;

    }
    return;
}
