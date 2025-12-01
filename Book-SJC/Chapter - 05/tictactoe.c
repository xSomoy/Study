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
    system("clear");
#endif
}

//  function prototypes

void drawBoard();
int showResult(char ch);
int validateInput(int cell);
void turnPlayerO(int *pCell);
void turnPlayerX(int *pCell);
int readCellFromStream(FILE *stream, int *outCell);
void getRowCol(int cell, int *pX, int *pY);

int main(int argc, char **argv)
{
    FILE *inputFile = NULL;
    int nonInteractive = 0;
    int x = 0,
        y = 0,
        row = 0,
        col = 0,
        selectedCell = 0,
        availableCell = 9;
    int xMoves = 0, oMoves = 0;

    char startChar = '1';
    if (argc > 1)
    {
        inputFile = fopen(argv[1], "r");
        if (inputFile == NULL)
        {
            perror("Opening moves file");
        }
        else
        {
            nonInteractive = 1;
        }
    }
    clearScreen();
    // make all the cell numbered from 1 to 9

    for (row = 0; row < 3; row++)
    {
        for (col = 0; col < 3; col++)
        {
            gameBoard[row][col] = startChar++;
        }
    }

    // now draw boar with current data in gameBoard[][] array
    if (!nonInteractive)
        clearScreen();
    drawBoard();
    fflush(stdout);

    // loop untill we'ev played all the cell

    while (availableCell > 0)
    {
        // assume Player One is X

        if (inputFile)
        {
            if (readCellFromStream(inputFile, &selectedCell) == 0)
            {
                break; // no more moves
            }
        }
        else
        {
            turnPlayerX(&selectedCell);
        }
        // get row and column from the selected selectedCell
        getRowCol(selectedCell, &x, &y);
        // update gameBoard array
        gameBoard[x][y] = 'X';
        xMoves += 1;
        // decrease available cell
        availableCell -= 1;
        // redraw gameboard with current data in gameBoard[][] array
        drawBoard();
        fflush(stdout);

        if (xMoves >= 3 && showResult('X') == 1)
        {
            break;
        }
        else if (availableCell == 0)
        {
            printf("\n Game Drawn");
            break;
        }
        if (inputFile)
        {
            if (readCellFromStream(inputFile, &selectedCell) == 0)
            {
                break; // no more moves
            }
        }
        else
        {
            turnPlayerO(&selectedCell);
        }
        getRowCol(selectedCell, &x, &y);
        gameBoard[x][y] = 'O';
        oMoves += 1;
        availableCell -= 1;
        if (!nonInteractive)
            clearScreen();
        drawBoard();
        fflush(stdout);
        if (oMoves >= 3 && showResult('O') == 1)
        {
            break;
        }
        else if (availableCell == 0)
        {
            printf("\n Game Drawn");
            break;
        }
    }
    if (inputFile)
        fclose(inputFile);
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

int readCellFromStream(FILE *stream, int *outCell)
{
    int cell;
    if (fscanf(stream, "%d", &cell) != 1)
        return 0;
    if (0 == validateInput(cell))
        return 0;
    *outCell = cell;
    return 1;
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