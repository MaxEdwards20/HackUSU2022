from player import HumanPlayer, RandomComputerPlayer
from game import TicTacToe, play

if __name__ == '__main__':
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    game = TicTacToe()
    play(game, x_player, o_player, True)
