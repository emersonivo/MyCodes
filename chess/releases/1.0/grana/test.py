import re
import os
import glob
from collections import defaultdict

global diag
global lins
global cols
global tmp
global homedir
global lastcel
global board

diag = defaultdict(list)
lins = defaultdict(list)
cols = defaultdict(list)
numlin = 0
numcol = 0
board = []
homedir = "/bkp_local/MyCodes/chess"
tmp = homedir + "/tmp"


def createboard(x, y):
    global numlin
    global numcol
    global lastcel
    numlin = x
    numcol = y
    lastcel = int(str(x) + str(y)) + 1
    for l in range(1, numlin + 1):
        for c in range(1, numcol + 1):
            board.append(str(l) + str(c))
    print("chessboard", board)

createboard(8,8)