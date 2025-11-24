#include <stdio.h>
int main()
{
    int x;
    printf("enter a number: ");
    scanf("%d", &x);
    if (x == 0)
        goto error;
    else
        printf("good");
    return 0;

error:
    printf("\n Error!");

    return 0;
}