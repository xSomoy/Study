#include <stdio.h>

int main()
{
    int score = 65;
    char grade;
    grade = (score >= 60) ? 'p' : 'f';
    printf("%c", grade);
    return 0;
}