#include <stdio.h>
#include <stdlib.h>

/* array to hold the cell status */
char gameBoard[3][3];

// cross-platform clear screen
void clearScreen(void)
{
#ifdef _WIN32
    system("cls");
#else
    clearScreen();
#endif
}

//  function prototypes

void drawBoard();
int showResult(char ch);
int validateInput(int cell);
void turnPlayerO(int *pCell);
void turnPlayerX(int *pCell);
void getRowCol(int cell, int *pX, int *pY);

int main()
{
    int x = 0,
        y = 0,
        row = 0,
        col = 0,
        selectedCell = 0,
        availableCell = 9;

    char startChar = '1';
    system("clear");
    // make all the cell numbered from 1 to 9

    for (row = 0; row < 3; row++)
    {
        for (col = 0; col < 3; col++)
        {
            gameBoard[row][col] = startChar++;
        }
    }

    // now draw boar with current data in gameBoard[][] array
    clearScreen();
    drawBoard();

    // loop untill we'ev played all the cell

    while (availableCell > 0)
    {
        // assume Player One is X

        turnPlayerX(&selectedCell);
        // get row and column from the selected selectedCell
        getRowCol(selectedCell, &x, &y);
        // update gemeBoard array
        gameBoard[x][y] = 'X';
        // decrease available cell
        availableCell -= 1;
        // redraw gameboard with current data in gameBoard[][] array
        drawBoard();

        if (showResult('X') == 1)
        {
            break;
        }
        else if (availableCell == 0)
        {
            printf("\n Game Drawn");
            break;
        }
        turnPlayerO(&selectedCell);
        getRowCol(selectedCell, &x, &y);
        gameBoard[x][y] = 'O';
        availableCell -= 1;
        clearScreen();
        drawBoard();
        if (showResult('O') == 1)
        {
            break;
        }
        else if (availableCell == 0)
        {
            printf("\n Game Drawn");
            break;
        }
    }
    return 0;
}

void drawBoard()
{
    int i, j;
    printf("\n TIC TAC TOE");
    printf("\n Digits (1-9) indicated VALID cel number \n");

    printf("\n      %c  |   %c  |   %c  ", gameBoard[0][0],
           gameBoard[0][1],
           gameBoard[0][2]);

    printf("\n      %c  |   %c  |   %c  ", gameBoard[1][0],
           gameBoard[1][1],
           gameBoard[1][2]);

    printf("\n      %c  |   %c  |   %c  ", gameBoard[2][0],
           gameBoard[2][1],
           gameBoard[2][2]);
}

void turnPlayerO(int *pCell)
{
    int cell;
    do
    {
        printf("\n Player O, \n Select VALID cell number: ");
        scanf("%d", &cell);
    } while (0 == validateInput(cell));

    *pCell = cell;
}

void turnPlayerX(int *pCell)
{
    int cell;
    do
    {
        printf("\n Player X, \n Select VALID cell number: ");
        scanf("%d", &cell);
    } while (0 == validateInput(cell));

    *pCell = cell;
}

void getRowCol(int cell, int *pX, int *pY)
{
    *pX = (cell - 1) / 3;
    *pY = (cell - 1) % 3;
}

int validateInput(int cell)
{
    int row, col;
    if ((cell < 1) || (cell > 9))
    {
        return 0;
    }
    row = (cell - 1) / 3;
    col = (cell - 1) % 3;
    if ((gameBoard[row][col] == 'O') || (gameBoard[row][col] == 'X'))
    {
        return 0;
    }
    return 1;
}

int showResult(char ch)
{
    int status = 0;

    //  diagonal \ 
    if (gameBoard[0][0] == ch && gameBoard[1][1] == ch && gameBoard[2][2] == ch)
    {
        printf("\n Player %c is Winner", ch);
        status = 1;
    }

    //  diagonal /
    if (gameBoard[0][2] == ch && gameBoard[1][1] == ch && gameBoard[2][0] == ch)
    {
        printf("\n Player %c is Winner", ch);
        status = 1;
    }
    //  row 0
    if (gameBoard[0][0] == ch && gameBoard[0][1] == ch && gameBoard[0][2] == ch)
    {
        printf("\n Player %c is Winner", ch);
        status = 1;
    }
    //  row 1
    if (gameBoard[1][0] == ch && gameBoard[1][1] == ch && gameBoard[1][2] == ch)
    {
        printf("\n Player %c is Winner", ch);
        status = 1;
    }
    //  row 2
    if (gameBoard[2][0] == ch && gameBoard[2][1] == ch && gameBoard[2][2] == ch)
    {
        printf("\n Player %c is Winner", ch);
        status = 1;
    }
    //  col 0
    if (gameBoard[0][0] == ch && gameBoard[1][0] == ch && gameBoard[2][0] == ch)
    {
        printf("\n Player %c is Winner", ch);
        status = 1;
    }
    //  col 1
    if (gameBoard[0][1] == ch && gameBoard[1][1] == ch && gameBoard[2][1] == ch)
    {
        printf("\n Player %c is Winner", ch);
        status = 1;
    }
    //  col 2
    if (gameBoard[0][2] == ch && gameBoard[1][2] == ch && gameBoard[2][2] == ch)
    {
        printf("\n Player %c is Winner", ch);
        status = 1;
    }
    return status;
}