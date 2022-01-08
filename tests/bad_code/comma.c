int bfunc(int c ,int d)
{
    return c + d;
}

int func(int h)
{
    return bfunc(h,h);
}

int foo(int a)
{
    for (int i = 0 ,e = a; i < e; i++);
    return a;
}
