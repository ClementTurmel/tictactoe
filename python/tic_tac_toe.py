from enum import Enum

class Cell(Enum):
    EMPTY = "_"
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

winning_cells_list = [
    [1,2,3], [4,5,6], [7,8,9], #ligns
    [1,4,7], [2,5,8], [3,6,9], #columns
    [1,5,9], [3,5,7]           #diagonals
]          

class TicTacToeGameEnd:
    def __init__(self, TicTacToeGame, winner=None) -> None:
        self.grid = TicTacToeGame.grid
        self.winner = winner
    
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

        if self.grid[x][y] is Cell.EMPTY:
            self.grid[x][y] = self.player
        else:
            print(f"Can't play on cell {cell_number}")
            return self

        winner = self.check_grid_for_winner()

        if winner:
            return TicTacToeGameEnd(self, winner)
        elif self.is_grid_full():
            return TicTacToeGameEnd(self)
        else:
            self.__move_to_next_player()
            return self
    
    def __move_to_next_player(self):
        self.player = Cell.ROUND if self.player == Cell.CROSS else Cell.CROSS


    def check_grid_for_winner(self):
        for winning_cells in winning_cells_list:
            if self.__is_same_cells_value(winning_cells):
                return self.__get_cell(winning_cells[0])
        
        return False
    
    def is_grid_full(self):
        return all(True if Cell.EMPTY not in lign else False for lign in self.get_grid())
        
    def __get_cell(self, cell_number:int):
        x, y = cell_to_x_y[cell_number]
        return self.grid[x][y]
    
    def __is_same_cells_value(self, cells:list()):
        values = [self.__get_cell(value) for value in cells]

        if Cell.EMPTY in values:
            return False

        return all(value == values[0] for value in values)