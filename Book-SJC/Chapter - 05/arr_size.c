#include <stdio.h>
#define ARR_SIZE 5

int main(void)
{
    int array[ARR_SIZE] = {10, 20, 30, 40, 50};
    int i;
    for (i = 0; i < ARR_SIZE; i++)
        printf("\n array[%d] is %d", i, array[i]);
    return 0;
}