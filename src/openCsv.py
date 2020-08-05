import csv

#Sudoku class 
class Sudoku:


    def __init__(self,sudoku_file,sudoku_game_number):
        self.sudoku_file = sudoku_file
        self.sudoku_game_number = sudoku_game_number
        self.sudoku_board = []
        with open(sudoku_file,"r") as archivo:
            archivo_csv = csv.reader(archivo)
            for game in archivo_csv:
                if not self.sudoku_game_number: 
                    board = list(map(int, game[0]))
                    self.sudoku_board = list(board[n:n + 9] for n, i in enumerate(board) if n % 9 == 0)
                    break
                self.sudoku_game_number-=1
            
    def get_board(self):
        return self.sudoku_board



