#include <stdio.h>
int main(void)
{
    int i, *ptr, odd[5] = {1, 3, 5, 7, 9};
    ptr = odd;

    for (i = 0; i < 5; i++)
    {
        printf("%d", *ptr);
        ptr++;
    }

    return 0;
}