def run():
    from TicTacToe.player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
    from TicTacToe.game import TicTacToe, play
    x_player = HumanPlayer("X")
    o_player = GeniusComputerPlayer("O")
    game = TicTacToe()
    play(game, x_player, o_player, True)

if __name__ == '__main__':
    run()