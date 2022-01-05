int a(void)
{
    int a = 0;

    if (1 == 0)
        if (0 == 1)
            if (2 == 5)
                a = 5;
    return a;
}

int calcult_lenth(int b, int c, int d)
{
    return (b + c + d);
}

int b(void)
{
    int a = 0;

    if (1 == 0)
        if (2 == 1)
            calcult_lenth(
                    a, 5, 6);
    return (a);
}
