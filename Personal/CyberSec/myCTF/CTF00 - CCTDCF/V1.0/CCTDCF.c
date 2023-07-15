#include <stdio.h>
int main()

{
    char flaw = "15435698";
    int flag = 15435698;
    int input;
    printf("CDCF v1.0\n");
    printf("This is an unofficial CTF challenge build by \"John Deadman\"\n");
    printf("Social: @xSomoy\n----------------------------------------------------------\n\n");
    printf("Hint: Find The 8 Digit Code to Get the Flag.\n\n");
    tryAgain:
    printf("Input The Code: ");
    scanf("%d",&input);
    if (input == flag )
        printf("\nCongratulations!!! You Found The Flag\nLet Me know how you found it. DM me on social\n\n");
    else {
        printf("\nSorry! This Is Not The Flag\nTry Again \n");
        goto tryAgain;
    }
    getch();
}
