int *abc(char *c, int a)
{
    if (!(*c))
        return &a;
    // int* a
    return &a;
}

void abd(int *i)
{
    static char tab[] = "something";

    if (tab[*i] == 'o')
        return;
}
