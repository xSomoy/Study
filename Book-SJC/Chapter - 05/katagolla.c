/*
TODO:
1. Draw a gameBoard

*/

#include <stdio.h>

void gameLoop();
void drawBoard();
void slotsPolatation(char *slots);

char slots[3][3];
int main()
{
    /*Game Driver*/
    gameLoop();
    return 0;
}

void gameLoop()
{
    drawBoard();
};

void slotsPolatation(char *slots)
{
    int i, j, m = 1;
    for (i = 0; i < 3; i++)
    {
        slots[i][0] = m;
        m++;
    }
}
void drawBoard()
{
    printf("\n TIC TAC TOE");
    printf("\n Digits (1-9) indicated VALID cel number \n");

    printf("\n      %c  |   %c  |   %c  ", slots[0][0],
           slots[0][1],
           slots[0][2]);

    printf("\n      %c  |   %c  |   %c  ", slots[1][0],
           slots[1][1],
           slots[1][2]);

    printf("\n      %c  |   %c  |   %c  ", slots[2][0],
           slots[2][1],
           slots[2][2]);
}