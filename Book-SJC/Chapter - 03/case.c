#include <stdio.h>
int main()
{
    int score, grade;
    printf("Enter Your Score:");
    scanf("%d", &score);
    grade = score / 10;
    switch (grade)
    {
    case 10:
    case 9:
        printf("Your Grade is A");
        break;
    case 8:
        printf("Your grade is B");
        break;
    case 7:
        printf("Your grade is C");
        break;
    case 6:
        printf("Your grade is D");
        break;
    default:
        printf("Your grade is F");
        break;
    }
    return 0;
}