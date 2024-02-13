from tic_tac_toe import TicTacToeGame, TicTacToeWinner



def show_grid(grid):
    #string_grid =" _ _ _ \n"
    string_grid = ""
    for lign in grid:
        #string_grid +="|"
        for cell in lign:
            string_grid += f"{cell.value}"
        string_grid +="\n"
    print(string_grid)


if __name__ == '__main__':
    print("Welcome to tic tac toe game ! ")
    game = TicTacToeGame()
    while not isinstance(game, TicTacToeWinner):
        show_grid(game.get_grid())
        player_input = input(f"player {game.player.value} it's your turn :")
        game = game.play(int(player_input))

    show_grid(game.get_grid())
    print(f"player {game.get_winner().value} win !")