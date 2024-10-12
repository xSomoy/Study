#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void main(){
    float area, radius, pi;
    char ch;
    system("clear");
    pi = 3.14259;
    printf("\nDo you want to calculate aread?(y/n): ");
    ch = getchar(); //getch alternative
    ch = toupper(ch);
    while(ch != 'N'){
        system("clear");
        printf("\n What's your radius?: ");
        scanf("%f", &radius);
        area = pi*radius*radius;
        printf("\n\nArea of a circle is: %.2f.",area);
        printf("\n\nDo you want to calculate area?(y/n): ");
        /* ch = getchar();
        For some reason using getfhar() does not works properly.
        it skips sometimes. so alternative is scanf() */
        scanf("%s",&ch);
        ch = toupper(ch);
    }
}
// Mushphyqur Rahman Tanveer
