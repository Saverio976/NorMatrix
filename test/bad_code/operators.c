int* abc(char *vk)
{
    return (int *) (char*) vk;
}

char **abc(char *av)
{
    char *new=av;

    if (av&av)
        return &av;
    return &av;
}
