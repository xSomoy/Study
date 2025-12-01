#include <stdio.h>
#include <stdlib.h>
void main(){
    system("clear");
    printf("\n\t Integer    type data takes %d byte, \a", sizeof(int));
    printf("\n\t Character  type data takes %d byte, \a", sizeof(char));
    printf("\n\t Float      type data takes %d byte, \a", sizeof(float));
    printf("\n\t Double     type data takes %d byte. \a", sizeof(double));
    char ch = getchar(); // alternative for getch()
}

// Mushphyqur Rahman Tanveer
