##### Test tic tac toe game should return grid with empt cells:

Given TicTacToe game

Then we have grid:
| | | |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |


##### Test tic tac toe game player can play at cell 1:

Given TicTacToe game

When player X plays 1

Then we have grid:
| | | |
|---|---|---|
| X | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |


##### Test tic tac toe game player can play at cell 5:

Given TicTacToe game

When player X plays 5

Then we have grid:
| | | |
|---|---|---|
| 1 | 2 | 3 |
| 4 | X | 6 |
| 7 | 8 | 9 |


##### Test when play is called two times we have a cross and a round:

Given TicTacToe game

When player X plays 7

When player O plays 9

Then we have grid:
| | | |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| X | 8 | O |


##### Test when play is called to time one same cell second play is not taken into account:

Given TicTacToe game

When player X plays 7

When player O plays 7

Then we have grid:
| | | |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| X | 8 | 9 |


##### Test all play instruction are executed with have a winner:

Given TicTacToe game

When player X plays 1

When player O plays 4

When player X plays 2

When player O plays 5

When player X plays 3

Then we have grid:
| | | |
|---|---|---|
| X | X | X |
| O | O | 6 |
| 7 | 8 | 9 |


Then we have winner: X

##### Test all play instruction are executed with have a winner:

Given TicTacToe game

When player X plays 1

When player O plays 4

When player X plays 2

When player O plays 5

When player X plays 9

When player O plays 6

Then we have grid:
| | | |
|---|---|---|
| X | X | 3 |
| O | O | O |
| 7 | 8 | X |


Then we have winner: O

##### Test game end is full most return true with a full grid:

Given TicTacToe game

When we set grid to :
| | | |
|---|---|---|
| X | X | O |
| O | O | X |
| X | X | O |


We  have a full grid

##### Test game end is full most return false with a non full grid:

Given TicTacToe game

When we set grid to :
| | | |
|---|---|---|
| 1 | 2 | O |
| O | O | X |
| X | X | O |


We do not have a full grid

##### Test there is 8 way to win:

Given TicTacToe game

When we set grid to :
| | | |
|---|---|---|
| X | X | X |
| 4 | 5 | 6 |
| 7 | 8 | 9 |


Then winner is : X

##### Test there is 8 way to win:

Given TicTacToe game

When we set grid to :
| | | |
|---|---|---|
| 1 | 2 | 3 |
| X | X | X |
| 7 | 8 | 9 |


Then winner is : X

##### Test there is 8 way to win:

Given TicTacToe game

When we set grid to :
| | | |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| X | X | X |


Then winner is : X

##### Test there is 8 way to win:

Given TicTacToe game

When we set grid to :
| | | |
|---|---|---|
| X | 2 | 3 |
| X | 5 | 6 |
| X | 8 | 9 |


Then winner is : X

##### Test there is 8 way to win:

Given TicTacToe game

When we set grid to :
| | | |
|---|---|---|
| 1 | X | 3 |
| 4 | X | 6 |
| 7 | X | 9 |


Then winner is : X

##### Test there is 8 way to win:

Given TicTacToe game

When we set grid to :
| | | |
|---|---|---|
| 1 | 2 | X |
| 4 | 5 | X |
| 7 | 8 | X |


Then winner is : X

##### Test there is 8 way to win:

Given TicTacToe game

When we set grid to :
| | | |
|---|---|---|
| X | 2 | 3 |
| 4 | X | 6 |
| 7 | 8 | X |


Then winner is : X

##### Test there is 8 way to win:

Given TicTacToe game

When we set grid to :
| | | |
|---|---|---|
| 1 | 2 | X |
| 4 | X | 6 |
| X | 8 | 9 |


Then winner is : X

