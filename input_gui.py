from sudoku_solver import Sudoku
import tkinter as tk
from tkinter import *

root = Tk()
root.title("Sudoku Solver")

grid = []

for i in range(9):
    row = []
    for j in range(9):
        e = Entry(
            width = 1,
        )
        e.grid(
            row = i, 
            column = j, 
            sticky = NSEW, 
            padx = 10, 
            pady = 5,
        )
        e.insert(END, 0)
        row.append(e)
    grid.append(row)

def onPress():
    for i in range(len(grid)):
        for j in range(len(row)):
            grid[i][j] = int(grid[i][j].get())
    puzzle = Sudoku(grid)
    puzzle.solve()

Button(
    text = "Solve", 
    command = onPress, 
    bg = "#5498F6", 
    fg = "#FFFFFF",
).grid(
    columnspan = 10,
)

root.mainloop()