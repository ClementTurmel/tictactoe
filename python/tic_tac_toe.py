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


class TicTacToeWinner:
    def __init__(self, TicTacToeGame) -> None:
        self.grid = TicTacToeGame.grid
        self.winner = TicTacToeGame.player
    
    def get_grid(self):
        return self.grid
    
    def get_winner(self):
        return self.winner

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

        have_a_winner = self.__check_grid()

        if have_a_winner:
            return TicTacToeWinner(self)
        else:
            self.__move_to_next_player()
            return self
    
    def __move_to_next_player(self):
        if self.player == Cell.CROSS:
            self.player = Cell.ROUND
        else:
            self.player = Cell.CROSS

    def __check_grid(self):
        if self.__get_cell(1) == self.__get_cell(2) == self.__get_cell(3) and self.__get_cell(1) is not Cell.EMPTY:
            return self.__get_cell(1)
        else:
            return None
        
    def __get_cell(self, cell_number:int):
        x, y = cell_to_x_y[cell_number]
        return self.grid[x][y]

