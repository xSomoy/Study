#include <stdio.h>
#include <stdlib.h>
void main(){
    float cent, farn;
    system("clear");
    printf("\nEnter temperature is centigrade: ");
    scanf("%f",&cent); /* get centrigrade value */
    farn = 1.8*cent+32;     /* do calculation */
    printf("\nFarenheit equivalent is : %.2f",farn);
    getchar();
}

// Mushphyqur Rahman Tanveer
