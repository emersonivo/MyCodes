import re
import os
import glob
import logging
logging.basicConfig(filename='log_filename.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('This is a log message.')

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
delcels = defaultdict(list)
lincol = 0
N_ = 8
numlin = numcol = N_
lastcell = int(str(numlin) + str(numcol))
homefolder = "/bkp_local/MyCodes/chess/releases/1.1/"
boardfile = homefolder+"/board.txt"
nKey = beg = end = p = 0
TMP_board = Next_board = ""
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
    # print(boards[1])
    # print(len(boards[1]))

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
    # print("XYZ: ", lines)

def check_board(y):
    TMP_board = boards[y]
    nKey = y + 1

    Num = TMP_board[0]
    print("Num ", Num)
    TMP_board.remove(TMP_board[0])
    boards[y] = TMP_board
    print("boards[",y,"]",  boards[y])
    print("TMP_board ", TMP_board)
    LastNum = Num

    r = 0
    for key, value in lines.items():
        if Num in value:
            line = lines[key]
            print(len(line), " Line: ", line)
            for r in line:
                if r in TMP_board:
                    TMP_board.remove(r)
    print("TMP_board ", TMP_board)
    if len(TMP_board) == 0:
        print("Recovering board ", y)
        boards[nKey] = boards[y -1]
    else:
        boards[nKey] = TMP_board

def getmillioprize():
    i = 1
    while len(boards[1] > (N_ - 1) or len(boards[N_] == 0:
        sizex = len(boards[i])
        if i > 1 and sizex <  (N_ - i):
            i = i - 1
        else:
            i = i + 1
            check_board(i)

createboard()
getlines()
getmillioprize()
#check_board(1)