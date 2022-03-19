/*
** EPITECH PROJECT, 2022
** h
** File description:
** h
*/

int abc(
                int a,
                int b
        )
{
    if (a == b)
        if (b == a)
            a = a + 1;
    if (b == a)
        if (a == b)
            b = a + 1;
    return a + b;
}
