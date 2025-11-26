#include <stdio.h>
long int find_factorial(long int n)
{
    if (n <= 1)
        return 1;
    else
        return (n * find_factorial(n - 1));
}
int main(void)
{
    long int x;
    int n;
    printf("Enter Number: ");
    scanf("%d", &n);
    x = find_factorial(n);
    printf("\nFactorial of %d is : %ld", n, x);
    return 0;
}