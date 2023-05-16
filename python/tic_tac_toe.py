from enum import Enum

class TicTacToeGame:

    def grid(self):
        return [
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY],
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY],
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY]
        ]
    
class Cell(Enum):
    EMPTY = " "