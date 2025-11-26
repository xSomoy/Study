#include <stdio.h>

int testFunc(int);

int main()
{
    int b = 4;
    testFunc(4);
    return 0;
}

int testFunc(int a)
{
    printf("%d", a);
}