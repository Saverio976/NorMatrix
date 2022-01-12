void av(char *ab, char *ac)
{
    if (&ab == &ac) {
        return;
    }
}

void *gh(int *i, char *ab)
{
    if (ab[*i] == 'c') {
        (*i)++;
    }
    return 0;
}
