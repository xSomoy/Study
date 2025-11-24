#include <stdio.h>
int main()
{
    int x, a, b;
    x = 10, a = 5, b = 15;
    printf("   --x   --a    --b\n");
    printf("----------------------\n");

    while (--a, --b, --x)
    {
        printf("%6d %6d %6d\n", x, a, b);
    }
    return 0;
}