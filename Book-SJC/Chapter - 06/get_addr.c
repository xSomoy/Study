#include <stdio.h>
int main()
{
    int id = 44;
    float gpa = 3.87;
    float cgpa = 3.78;

    printf("Address of id is %x.\n", &id);
    printf("Address of id is %x.\n", &gpa);
    printf("Address of id is %x.\n", &cgpa);

    return 0;
}