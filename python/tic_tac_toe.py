from enum import Enum

class TicTacToeGame:

    def grid(self):
        return [
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY],
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY],
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY]
        ]
    
    def play(self, cell_number:int):
        return self
    
class Cell(Enum):
    EMPTY = " "
    CROSS = "X"
    ROUND = "O"