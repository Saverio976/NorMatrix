int a(int b, int c)
{
    for (int i = 0; i < b; i++);
    if (b == c) {
        b += c; return b;
    }
    return b;
}
