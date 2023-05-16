import pytest
from tic_tac_toe import TicTacToeGame, Cell

#python -m pytest .\test_tic_tac_toe.py

def test_true():
    assert True

def test_tic_tac_toe_game_shoul_return_grid_with_empt_cells():

    expected = [
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY],
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY],
            [Cell.EMPTY,Cell.EMPTY,Cell.EMPTY]
    ]

    assert TicTacToeGame().grid() == expected