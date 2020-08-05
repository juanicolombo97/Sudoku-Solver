# Imports
from random import randint
from openCsv import Sudoku
from game_gui import start_gui


#------------------------MAIN FUNCTION-----------------------

def main():
    # Get sudoku board
    sudoku_board = Sudoku("../sudoku.csv",randint(1,10000)).get_board()
    start_gui(sudoku_board)
main()