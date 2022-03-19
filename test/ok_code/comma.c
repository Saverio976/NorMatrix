/*
** EPITECH PROJECT, 2022
** h
** File description:
** h
*/

int func(int c, int d)
{
    return c + d;
}

int func2(int h)
{
    return func(h, h);
}

// a,b
/*
** a,b
*/

int func3(int a)
{
    func(func(a, a), func(a, a));
    return a;
}
