#include <stdio.h>

void main(){
    int pstv_range = 2147483647; // store 2147483647 to pstv_range variable
    int ngtv_range = -2147483648; // store -2147483648 to ngtv_range variable
    printf("\n %d + 1 is %d.\n",pstv_range,pstv_range + 1);
    printf("\n - %d - 1 is %d.\n", ngtv_range, ngtv_range - 1);
    char ch = getchar();
}
// modern compiler uses 4 byte for int thats why the range is -2,147,483,648 to 2,147,483,647

// Mushphyqur Rahman Tanveer
