import pytest
from tic_tac_toe import TicTacToeGame, Cell

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

def test_true():
    assert True

def test_tic_tac_toe_game_should_return_grid_with_empt_cells():

    expected = [
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY],
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY],
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY]
    ]
    game = TicTacToeGame()
    assert game.get_grid() == expected

def test_tic_tac_toe_game_player_can_play_at_cell_1():

    expected = [
            [X,_,_],
            [_,_,_],
            [_,_,_]
    ]

    assert TicTacToeGame().play(1).get_grid() == expected

def test_tic_tac_toe_game_player_can_play_at_cell_5():

    expected = [
            [_,_,_],
            [_,X,_],
            [_,_,_]
    ]

    assert TicTacToeGame().play(5).get_grid() == expected


def test_when_play_is_called_to_time_we_have_a_cross_and_a_round():

    expected = [
            [_,_,_], # 1 2 3 
            [_,_,_], # 4 5 6 
            [X,_,O]  # 7 8 9 
    ]

    assert TicTacToeGame().play(7).play(9).get_grid() == expected