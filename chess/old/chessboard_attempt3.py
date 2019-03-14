import re
import os
import glob
from collections import defaultdict

global lines
global tmp
global homedir
global lastcel
global board
global lincol

lines = defaultdict(list)
d = dict()
boards = defaultdict(list)
line = []
lincol = 0
N_ = 8
numlin = numcol = N_
lastcell = int(str(numlin) + str(numcol))
homefolder = "/bkp_local/MyCodes/chess"
boardfile = homefolder+"/board.txt"
beg = end = p = 0
Q1_board = Q2_board = Q3_board = Q4_board = Q5_board = Q6_board = Q7_board = Q8_board = []
LastQ1 = LastQ2 = LastQ3 = LastQ4 = LastQ5 = LastQ6 = LastQ7 = LastQ8 = []
rangecol = rangelin = range(1,N_ + 1)


def createboard(): #GOOD
    for l in rangelin:
        for c in rangecol:
            lincol = int(str(l) + str(c))
            boards[0].append(lincol)
    #board[1] = board
    print(boards[0])
    boards[1] = boards[0]
    print(boards[1])
    print(len(boards[1]))

def getlines(): # GOOD
    for l in rangelin:
        for c in rangecol:
            if l == 1 and c== 1:
                lincol = int(str(l) + str(c))
                for cel in range(11, lastcell + 1 , 11):
                    lines[str(lincol)].append(cel)
            elif l == 1 and c > 0:
                beg = int(str(l) + str(c))
                end = (lastcell + 10) - ( c * 10) + 1
                lincol = int(str(l) + str(c))
                for cel in range(beg, end, 11):
                    lines[str(lincol)].append(cel)
            elif l > 0 and c == 1: #
                lincol = int(str(l) + str(c))
                beg = int(str(l) + str(c))
                end = int(str(c) + str(l)) - 1
                for cel in range(beg, end, -9):
                    lines[str(lincol)].append(cel)
            elif l >=1 and c == N_:
                lincol = int(str(l) + str(c))
                beg = int(str(l) + str(c))
                end = (int(str(c) + str(l))) + 1
                for cel in range(beg, end, 9):
                    lines[str(lincol)].append(cel)
            elif l == N_ and c > 0:
                lincol = int(str(l) + str(c))
                beg = int(str(l)+str(c))
                e1 = l - c
                e2 = l - 1
                end = int(str(e1) + str(e2))
                for cel in range(beg, end, -11):
                    lines[str(lincol)].append(cel)
    for l in rangelin:
        for c in rangecol:
            cel = int(str(l) + str(c))
            lines["L" + str(l)].append(cel)

    for c in rangecol:
        for l in rangelin:
            cel = int(str(l) + str(c))
            lines["C" + str(c)].append(cel)
    print(lines)

def check_board(self, i):


def getmillioprize():
    Exit = 0
    while Exit == 0:
        x = 1
        for i in range(x, N_ + 1):
            check_board(i)
            if len(boards[i]) < (N_ - i):
                i -= 1
                print("True")
            elif len(boards[i]) <= N_ -1:
                Exit == 1
            elif len(boards[N_]) > 0:
                Exit == 1


createboard()