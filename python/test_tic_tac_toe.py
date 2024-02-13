import pytest
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
        [_,_,_], # 1 2 3
        [_,X,_], # 4 5 6
        [_,_,_]  # 7 8 9
    ]

    assert TicTacToeGame().play(5).get_grid() == expected


def test_when_play_is_called_to_time_we_have_a_cross_and_a_round():
    expected = [
        [_,_,_], # 1 2 3
        [_,_,_], # 4 5 6
        [X,_,O]  # 7 8 9
    ]

    assert TicTacToeGame()\
        .play(7)\
        .play(9)\
        .get_grid() == expected


def test_when_play_is_called_to_time_one_same_cell_second_play_is_not_taken_into_account():
    expected = [
        [_,_,_], # 1 2 3
        [_,_,_], # 4 5 6
        [X,_,_]  # 7 8 9
    ]

    assert TicTacToeGame()\
        .play(7)\
        .play(7)\
        .get_grid() == expected


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
def test_all_play_instruction_are_executed_with_have_a_winner(play_instructions, expected_winner, expected_grid):
    game = TicTacToeGame()

    for instruction_cell in play_instructions:
        game = game.play(instruction_cell)

    assert game.get_grid()   == expected_grid
    assert game.get_winner() == expected_winner

    
def test_game_end_is_full_most_return_true_with_a_full_grid():
    game = TicTacToeGame()
    game.grid = [
        [X,X,O], # 1 2 3
        [O,O,X], # 4 5 6
        [X,X,O]  # 7 8 9
    ]

    assert game.is_grid_full()

def test_game_end_is_full_most_return_false_with_a_non_full_grid():
    game = TicTacToeGame()
    game.grid = [
        [_,_,O], # 1 2 3
        [O,O,X], # 4 5 6
        [X,X,O]  # 7 8 9
    ]

    assert game.is_grid_full() is False



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
def test_there_is_8_way_to_win(grid):
    game = TicTacToeGame()
    game.grid = grid
    assert game.check_grid_for_winner() == Cell.CROSS



