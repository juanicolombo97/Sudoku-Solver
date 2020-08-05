class Board:

    def __init__(self, board, length):
        self.board = board
        self.length = length

    def add_number(self, row, col, number):
        self.board[row][col] = number

    def delete_number(self, row, col):
        self.board[row][col] = 0

    def get_board(self):
        return self.board
        
    def get_length(self):
        return self.length