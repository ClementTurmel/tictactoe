import pytest
from tic_tac_toe import TicTacToeGame, Cell

#https://codingdojo.org/kata/tic-tac-toe/

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

def test_tic_tac_toe_game_player_can_play():

    expected = [
            [X,_,_],
            [_,_,_],
            [_,_,_]
    ]

    assert TicTacToeGame().play(1).get_grid() == expected