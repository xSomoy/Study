#include <stdio.h>

void main(void){
    float a = 10.375;
    char *p;
    int i;

    p = ( char * ) &a;
    for( i = 0; i<=3; i++)
        printf("%02x ", (unsigned char) p[i]);
}

// Mushphyqur Rahman Tanveer
