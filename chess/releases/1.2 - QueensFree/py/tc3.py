import itertools
import datetime
now = datetime.datetime.now()
timex = now.strftime('%Y%m%d%H%M%S')
from collections import defaultdict
from pathlib import Path

global lines
global tmp
global homedir
global lastcel
global board
global lincol
global sair

dict = list
done = False
lines = defaultdict(list)
d = dict()
boards = defaultdict(list)
delcels = defaultdict(list)
t = 0
lincol = 0
g = 0
#N_ = 8
global i

homefolder = "/bkp_local/MyCodes/chess/releases/1.1/"
boardfile = homefolder + "/board.txt"
nKey = beg = end = p = 0
tmp_board = tmp1 = tmp2 = Next_board = []
LastQ = []

def createboard(N_):  # GOOD
    numlin = numcol = N_
    lastcell = int(str(numlin) + str(numcol))
    #print("#1")
    for l in range(1, N_ + 1):
        for c in range(1, N_ + 1):
            print("Col", l, c)
            lincol = str(l) + "." + str(c)
            boards[0].append(lincol)
    #print(boards[0])
    boards[1] = boards[0]
    print(" # ",N_, boards[0])
    exit
def get_combinations(N_):
    rangecol = rangelin = range(1, N_ + 1)
    numlin = numcol = N_
    lastcell = int(str(numlin) + str(numcol))
    i = 2
    while True:
        while i > 0:
            i = i - 1
            ##print(len(boards[i]), i, len(boards[i]) > (N_ - i + 1), i > 0)
            while len(boards[i]) > (N_ - i + 1) and i > 0:
                # CRIANDO PRÓXIMO TABULEIRO
                tmp1 = tmp2 = tmp_board = []
                tmp1.insert(0, boards[i])
                tmp_board = list(itertools.chain(*tmp1))
                num = tmp_board[0]
                #print("0 - ", num)
                if len(LastQ) >= i:
                    LastQ.pop(i - 1)
                    LastQ.insert(i - 1, num)

                else:
                    LastQ.insert(i - 1, num)

                tmp_board.remove(tmp_board[0])
                #print("1 ", i, boards[i])
                del boards[i]
                for r in tmp_board:
                    boards[i].append(r)
                #print("2 ", i, boards[i])

                if i + 1 > N_:
                    nKey = i
                else:
                    nKey = i + 1
                #print("3 - Next boards ", nKey)
                # SELECIONANDO CELULAS BLOQUEADAS
                r = 0
                cel = num.split(".")
                l = int(cel[0])
                c = int(cel[1])
                line = []
                if l <= N_:  # Diagonais para direita/abaixo  GOOD
                    while l <= N_ and c <= N_:
                        cell = str(l) + "." + str(c)
                        line.append(cell)
                        l = l + 1
                        c = c + 1

                l = int(cel[0])
                c = int(cel[1])
                if c > 1:  # Diagonais para direita/acima
                    while c >= 1 and l >= 1:
                        cell = str(l) + "." + str(c)
                        line.insert(0, cell)
                        l = l - 1
                        c = c + 1

                l = int(cel[0])
                c = int(cel[1])
                if c > 1:  # Diagonais para esquerda/acima   GOOD
                    while c >= 1 and l >= 1:
                        cell = str(l) + "." + str(c)
                        line.insert(0, cell)
                        l = l - 1
                        c = c - 1

                l = int(cel[0])
                c = int(cel[1])
                if l < N_ and c > 1:  # Diagonais para esquerda/abaixo  GOOD
                    while l <= N_ and c >= 1:
                        cell = str(l) + "." + str(c)
                        line.append(cell)
                        l = l + 1
                        c = c - 1

                l = int(cel[0])
                c = int(cel[1])
                if c > 1:  # Horizontal para a esquerda
                    while c >= 1:
                        cell = str(l) + "." + str(c)
                        line.insert(0, cell)
                        c = c - 1

                l = int(cel[0])
                c = int(cel[1])
                if c < N_:  # Horizontal para a direita
                    while c <= N_:
                        cell = str(l) + "." + str(c)
                        line.append(cell)
                        c = c + 1

                l = int(cel[0])
                c = int(cel[1])
                if l > 1:  # Vertical para cima
                    while l >= 1:
                        cell = str(l) + "." + str(c)
                        line.append(cell)
                        l = l - 1

                l = int(cel[0])
                c = int(cel[1])
                if l < N_:  # Vertical para cima
                    while l <= N_:
                        cell = str(l) + "." + str(c)
                        line.append(cell)
                        l = l + 1

                # REMOVENDO CELULAS BLOQUEADAS DO PROXIMO TABULEIRO
                #print("4 - To be removed from boards[",nKey,"]", line)
                for r in line:
                    if r in tmp_board:
                        tmp_board.remove(r)

                # CHECANDO TAMANHO DO PROXIMO TABULEIRO
                #print("4.1 - tmp_board", tmp_board)
                if len(tmp_board) == 0:
                    #print("4.2 - tmp_board empty", tmp_board)
                    continue
                else:
                    if len(boards[nKey]) != 0:
                        del boards[nKey]
                    for r in tmp_board:
                        boards[nKey].append(r)
                    #print("5 - boards[",nKey,"]", boards[nKey])

                    # 1 - CONSTRUINDO PRÓXIMO TABULEIRO
                    # 2 - CHECANDO SE O PRÓXIMO TABULEIRO É O ULTIMO
                    # 3 - CRIANDO ARQUIVO DE OUTPUT
                    if nKey == N_ and len(boards[nKey]) > 0:
                        if len(LastQ) == nKey:
                            LastQ.pop(nKey - 1)
                        tmp1.insert(0, boards[nKey])
                        tmp_board = list(itertools.chain(*tmp1))
                        num = tmp_board[0]
                        LastQ.insert(nKey, num)
                        with open("myboard-" + str(N_) + "x" + str(N_) + "-" + timex + ".txt", 'at') as f:
                            for r in LastQ:
                                f.write(r + ";")
                            f.write("\n")

                    # CONFERINDO TAMANHO DO ARQUIVO DE OUTPUT
                    t = 0
                    f = Path("myboard-" + str(N_) + "x" + str(N_) + "-" + timex + ".txt")
                    if f.is_file():
                        with open("myboard-" + str(N_) + "x" + str(N_) + "-" + timex + ".txt", "rt") as f:
                            t = len(f.readlines())
                        if t > 4:
                            return False
                    if i < N_:
                        i = i + 1
                    elif i > 0 and i <= N_:
                        i = i - 1

                #print("6 - Next check boards[", i, "]")
        else:
            False
for N_ in range(8, 10):
    #rangecol = rangelin = range(1, N_ + 1)
    #numlin = numcol = N_
    #lastcell = int(str(numlin) + str(numcol))
    createboard(N_)
    get_combinations(N_)