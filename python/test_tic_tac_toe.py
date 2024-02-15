import pytest
from markdown_writter import *
from tic_tac_toe import TicTacToeGame, TicTacToeGameEnd, Cell

#https://codingdojo.org/kata/tic-tac-toe/
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+

#python -m pytest .\test_tic_tac_toe.py

X = Cell.CROSS
O = Cell.ROUND
_ = Cell.EMPTY


def test_tic_tac_toe_game_should_return_grid_with_empt_cells(doc):

    expected = [
        [_,_,_],
        [_,_,_],
        [_,_,_]
    ]
    
    grid = GivenTicTacToeGame(doc)\
        .we_have_grid()
    
    assert grid == expected

def test_tic_tac_toe_game_player_can_play_at_cell_1(doc):

    GivenTicTacToeGame(doc)\
        .when_we_play(1)\
        .we_expect_grid([
            [X,_,_],
            [_,_,_],
            [_,_,_]
        ])


def test_tic_tac_toe_game_player_can_play_at_cell_5(doc):

    GivenTicTacToeGame(doc)\
        .when_we_play(5)\
        .we_expect_grid([
            [_,_,_],
            [_,X,_],
            [_,_,_]
        ])


def test_when_play_is_called_two_times_we_have_a_cross_and_a_round(doc):
    GivenTicTacToeGame(doc)\
        .when_we_play(7)\
        .when_we_play(9)\
        .we_expect_grid([
            [_,_,_], # 1 2 3
            [_,_,_], # 4 5 6
            [X,_,O]  # 7 8 9
        ])



def test_when_play_is_called_to_time_one_same_cell_second_play_is_not_taken_into_account(doc):
    GivenTicTacToeGame(doc)\
        .when_we_play(7)\
        .when_we_play(7)\
        .we_expect_grid([
            [_,_,_], # 1 2 3
            [_,_,_], # 4 5 6
            [X,_,_]  # 7 8 9
        ])


@pytest.mark.parametrize("play_instructions, expected_winner, expected_grid", [
    (
        #X,O,X,O,X
        [1,4,2,5,3], X,   [[X,X,X], # 1 2 3
                           [O,O,_], # 4 5 6
                           [_,_,_]  # 7 8 9
        ]
    ),
    (
        #X,O,X,O,X,O
        [1,4,2,5,9,6], O, [[X,X,_], # 1 2 3
                           [O,O,O], # 4 5 6
                           [_,_,X]  # 7 8 9
        ]
    )
])
def test_all_play_instruction_are_executed_with_have_a_winner(play_instructions, expected_winner, expected_grid, doc):
    game = GivenTicTacToeGame(doc)

    for instruction_cell in play_instructions:
        game = game.when_we_play(instruction_cell)

    game.we_expect_grid(expected_grid)\
        .we_expect_winner(expected_winner)

    
def test_game_end_is_full_most_return_true_with_a_full_grid(doc):
    GivenTicTacToeGame(doc)\
    .when_we_set_grid_to([
        [X,X,O], # 1 2 3
        [O,O,X], # 4 5 6
        [X,X,O]  # 7 8 9
    ])\
    .we_expect_a_full_grid(is_full=True)

def test_game_end_is_full_most_return_false_with_a_non_full_grid(doc):
    GivenTicTacToeGame(doc)\
    .when_we_set_grid_to([
        [_,_,O], # 1 2 3
        [O,O,X], # 4 5 6
        [X,X,O]  # 7 8 9
    ])\
    .we_expect_a_full_grid(is_full=False)



@pytest.mark.parametrize("grid", [
    (
        [X,X,X], # 1 2 3
        [_,_,_], # 4 5 6
        [_,_,_]  # 7 8 9
    ),(
        [_,_,_], # 1 2 3
        [X,X,X], # 4 5 6
        [_,_,_]  # 7 8 9
    ),(
        [_,_,_], # 1 2 3
        [_,_,_], # 4 5 6
        [X,X,X]  # 7 8 9
    ),(
        [X,_,_], # 1 2 3
        [X,_,_], # 4 5 6
        [X,_,_]  # 7 8 9
    ),(
        [_,X,_], # 1 2 3
        [_,X,_], # 4 5 6
        [_,X,_]  # 7 8 9
    ),(
        [_,_,X], # 1 2 3
        [_,_,X], # 4 5 6
        [_,_,X]  # 7 8 9
    ),(
        [X,_,_], # 1 2 3
        [_,X,_], # 4 5 6
        [_,_,X]  # 7 8 9
    ),(
        [_,_,X], # 1 2 3
        [_,X,_], # 4 5 6
        [X,_,_]  # 7 8 9
    ),
])
def test_there_is_8_way_to_win(grid, doc):
    GivenTicTacToeGame(doc)\
    .when_we_set_grid_to(grid)\
    .we_expect_winner_to_be(Cell.CROSS)


########## HELPERS ##########

class GivenTicTacToeGameEnd(TicTacToeGameEnd):
    def __init__(self, game, winner, doc) -> None:
        self.doc = doc
        super().__init__(game, winner)

    def we_expect_grid(self, expected_grid):
        current_grid = self.get_grid()
        self.doc.log(f"Then we have grid:\n{build_grid(current_grid)}")
        assert_grid_equals(current_grid, expected_grid)
        return self
    
    def we_expect_winner(self, expected_winner):
        self.doc.log(f"Then we have winner: {self.get_winner().value}")
        assert self.get_winner() == expected_winner
        return self


class GivenTicTacToeGame(TicTacToeGame):
    def __init__(self, doc) -> None:
        self.doc = doc
        self.doc.log("Given TicTacToe game")
        super().__init__()
    
    def when_we_play(self, cell_number):
        self.doc.log(f"When player {self.player.value} plays {cell_number}")
        game = self.play(cell_number)

        if isinstance(game, TicTacToeGameEnd):
            return GivenTicTacToeGameEnd(game, game.winner, self.doc)
        else:
            return game
        

    def we_have_grid(self):
        self.doc.log(f"Then we have grid:\n{build_grid(self.get_grid())}")
        return self.get_grid()
    
    def we_expect_grid(self, expected_grid):
        current_grid = self.get_grid()
        self.doc.log(f"Then we have grid:\n{build_grid(current_grid)}")
        assert_grid_equals(current_grid, expected_grid)
        return self
    
    def when_we_set_grid_to(self, grid):
        self.doc.log(f"When we set grid to :\n{build_grid(grid)}")
        self.grid = grid
        return self

    def we_expect_a_full_grid(self, is_full):
        self.doc.log(f"We {'do not' if self.is_grid_full() == False else ''} have a full grid")
        assert self.is_grid_full() == is_full
        return self
    
    def we_expect_winner_to_be(self, expected_winner):
        self.doc.log(f"Then winner is : {self.check_grid_for_winner().value}")
        assert self.check_grid_for_winner() == expected_winner
        return self

    
def assert_grid_equals(current_grid, expected_grid):
    assert current_grid == expected_grid, f"""
current grid:\n{build_grid(current_grid)}
expected grid:\n{build_grid(expected_grid)}
    """

def build_grid(grid):
    string_grid = "| | | |\n"
    string_grid += "|---|---|---|\n"
    cell_number = 1

    for lign in grid:
        for cell in lign:
            value = cell.value if cell is not Cell.EMPTY else str(cell_number)
            string_grid += f"| {value} "
            cell_number += 1
        string_grid +=f"|\n"

    return string_grid

