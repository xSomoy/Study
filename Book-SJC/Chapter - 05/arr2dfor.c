#include <stdio.h>
#define ROW 3
#define COL 5

int main()
{
    int row, col;
    float array2d[ROW][COL] = {
        {1.0, 2.0, 3.0, 4.0, 5.0},
        {6.0, 7.0, 8.0, 9.0, 10.0},
        {11.0, 12.0, 13.0, 14.0, 15.0}};

    for (row = 0; row < ROW; row++)
    {
        for (col = 0; col < COL; col++)
        {
            printf("\n Element [%d] [%d] = %6.3f", row, col, array2d[row][col]);
        }
    }
    return 0;
};