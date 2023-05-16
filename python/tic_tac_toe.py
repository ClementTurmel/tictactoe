from enum import Enum

class Cell(Enum):
    EMPTY = " "
    CROSS = "X"
    ROUND = "O"


cell_to_x_y =    {
            1: (0,0),
            2: (0,1),
            3: (0,2),
            4: (1,0),
            5: (1,1),
            6: (1,2),
            7: (2,0),
            8: (2,1),
            9: (2,2)
}


class TicTacToeGame:

    
    
    def __init__(self) -> None:
        self.grid = [
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY],
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY],
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY]
        ]

        self.player = Cell.CROSS
    
    def get_grid(self):
        return self.grid
    
    def play(self, cell_number:int):

        x, y = cell_to_x_y[cell_number]
        self.grid[x][y] = self.player

        self.move_to_next_player()

        return self
    
    def move_to_next_player(self):
        if self.player == Cell.CROSS:
            self.player = Cell.ROUND
        else:
            self.player = Cell.CROSS
    