// variable scope test inside a fucntion
#include <stdio.h>

int print_msg(void)
{
    int x = 8;
    printf("%d", x);
    return x;
}

int main()
{
    int a;
    a = print_msg();
    printf("%d", a);

    return 0;
}