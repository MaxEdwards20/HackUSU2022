from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
from game import TicTacToe, play

if __name__ == '__main__':
    x_player = RandomComputerPlayer("X")
    o_player = GeniusComputerPlayer("O")
    game = TicTacToe()
    play(game, x_player, o_player, False)
