#include <stdio.h>

int main()
{
    int var;
    var = 1;
    printf("using postfix (var++) var = %d\n", var++); // postfix
    printf("Value After increment is: %d\n\n", var);
    var = 1;
    printf("using postfix (var++) var = %d\n", ++var); // prefix
    printf("Value After increment is: %d\n\n", var);
    return 0;
}