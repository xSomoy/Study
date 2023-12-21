// Popsicles Solution In C

#include <stdio.h>

int main() {
    int siblings, popsicles, de;
    scanf("%d", &siblings);
    scanf("%d", &popsicles);

    //your code goes here
    de = popsicles % siblings;
    if(de== 0){
        printf("give away");
    }
    else {
        printf("eat them yourself");
    }
    
    return 0;
}