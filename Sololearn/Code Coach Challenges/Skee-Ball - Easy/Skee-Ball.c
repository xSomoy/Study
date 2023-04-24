#include <stdio.h>

int main() {
    int score,ball,ticket;
    scanf("%d",&score);
    scanf("%d",&ball);
    ticket = score / 12;
    if(ticket < ball){
        printf("Try again");
    }
    else{
        printf("Buy it!");
    }

    return 0;
}