from SnakeCali.main import SnakeCali
from TicTacToe.main import run as runTicTac

def mainMenu():
    while True:
        print("Welcome to our Game Shop!")
        print("Your options are:\n\t1) Snake \n\t2) TicTacToe")
        while True:
            game = str(input("What game would you like to play? ")).strip()
            if game == '1' or '2':
                break
            else:
                print(f"{game} is an invalid input. Please enter 1 or 2.")
        if game == '1':
            SnakeCali().run()
        else:
            runTicTac()

if __name__ == "__main__":
    mainMenu()
