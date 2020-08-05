# Imports
from random import randint
from openCsv import Sudoku
from game_gui import start_gui
from tkinter import *


#------------------------MAIN FUNCTION-----------------------
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def start_menu(sudoku_board):
    root = Tk()
    root.title("Menu")
    root.geometry("400x600")
    center(root)
    
    filename = PhotoImage(file = "/Users/juanicolombo/Desktop/git/Sudoku-Solver/backgroung.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    timeLabel = Label(root, text="Enter max time for game: ")
    timeLabel.grid(padx=100,pady=10)


    timeSelected = Entry(root, width=20)
    timeSelected.grid(padx=100,pady=5)


    livesLabel = Label(root, text="Enter amount of lives: ")
    livesLabel.grid(padx=100,pady=10)


    livesSelected = Entry(root, width=20)
    livesSelected.grid(padx=100,pady=5)


    startButton = Button(root, text="Start Game", command=lambda: start_game(sudoku_board, root, int(timeSelected.get()), int(livesSelected.get())))
    startButton.grid(padx=100,pady=10)



    quitButton = Button(root, text="Quit", command=root.destroy)
    quitButton.grid(padx=100,pady=10)

    root.mainloop()

def start_game(sudoku_board, root, time, lives):
    root.destroy()
    resultado = start_gui(sudoku_board, time * 60, lives)
    ventana = Tk()
    ventana.title("Resultado")
    ventana.geometry("200x200")
    center(ventana)
    
    resultadoLabel = Label(ventana, text=resultado)
    resultadoLabel.pack()

    root.mainloop()

def main():
    # Get sudoku board
    sudoku_board = Sudoku("../sudoku.csv",randint(1,10000)).get_board()

    # Menu
    start_menu(sudoku_board)
    
main()