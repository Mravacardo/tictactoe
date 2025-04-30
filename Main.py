import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

sign = 0

global board
board = [[" " for x in range(3)] for y in range(3)]

def winner(b, l):
    return (
            (b[0][0] == 1 and b[0][1] == 1 and b[0][2] == 1) or
            (b[1][0] == 1 and b[1][1] == 1 and b[1][2] == 1) or
            (b[2][0] == 1 and b[2][1] == 1 and b[2][2] == 1) or
            (b[0][0] == 1 and b[1][0] == 1 and b[2][0] == 1) or
            (b[0][1] == 1 and b[1][1] == 1 and b[2][1] == 1) or
            (b[0][2] == 1 and b[1][2] == 1 and b[2][2] == 1) or
            (b[0][0] == 1 and b[1][1] == 1 and b[2][2] == 1) or
            (b[0][2] == 1 and b[1][1] == 1 and b[2][0] == 1)
    )

def get_text(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':

        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
        if winner(board, "X"):
            gb.destroy()
            box = messagebox.showinfo("Winner", "Player 1 won the match")
        elif winner(board, "O"):
            gb.destroy()
            box = messagebox.showinfo("Winner", "Player 2 won the match")
        elif (isfull()):
            gb.destroy()
            box = messagebox.showinfo("Tie Game", "Tie Game")


def isfree(i, j):
