from enum import Enum

class Cell(Enum):
    EMPTY = " "
    CROSS = "X"
    ROUND = "O"

class TicTacToeGame:

    def __init__(self) -> None:
        self.grid = [
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY],
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY],
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY]
        ]
    
    def get_grid(self):
        return self.grid
    
    def play(self, cell_number:int):

        self.grid[0][0] = Cell.CROSS

        return self
    
