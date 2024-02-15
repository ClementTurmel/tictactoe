from tic_tac_toe import TicTacToeGame, TicTacToeGameEnd, Cell

#python tic_tac_toe_game.py

grid_separator = "+---+---+---+"


def build_grid(grid):
    string_grid = F"{grid_separator}\n"
    cell_number = 1

    for lign in grid:
        for cell in lign:
            value = cell.value if cell is not Cell.EMPTY else str(cell_number)
            string_grid += f"| {value} "
            cell_number += 1
        string_grid +=f"|\n{grid_separator}\n"

    return string_grid


def show_grid(grid):
    print(build_grid(grid))


if __name__ == '__main__':
    print("Welcome to tic tac toe game ! ")
    game = TicTacToeGame()
    while not isinstance(game, TicTacToeGameEnd):
        show_grid(game.get_grid())
        player_input = input(f"player {game.player.value} it's your turn :")
        game = game.play(int(player_input))

    show_grid(game.get_grid())
    if game.get_winner() is not None:
        print(f"player {game.get_winner().value} win !")
    else:
        print("Equality")