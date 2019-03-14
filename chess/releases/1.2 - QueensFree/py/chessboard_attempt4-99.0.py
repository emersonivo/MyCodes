for N_ in range(8, 9):
    import re
    import os
    import glob
    import sys
    import itertools
    import datetime
    import logging
    logging.basicConfig(filename='log_filename.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.debug('This is a log message.')
    now = datetime.datetime.now()
    timex = now.strftime('%Y%m%d%H%M%S')
    from collections import defaultdict

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
    #N_ = 9
    global i
    i = 1
    numlin = numcol = N_
    lastcell = int(str(numlin) + str(numcol))
    homefolder = "/bkp_local/MyCodes/chess/releases/1.1/"
    boardfile = homefolder+"/board.txt"
    nKey = beg = end = p = 0
    tmp_board = tmp1 = tmp2 = Next_board = []
    LastQ = []
    rangecol = rangelin = range(1,N_ + 1)

    def createboard(): #GOOD
        for l in rangelin:
            for c in rangecol:
                lincol = str(l) + "." + str(c)
                boards[0].append(lincol)
        print(boards[0])
        boards[1] = boards[0]

    def check_board(y):
        tmp1 = tmp2 = tmp_board = []
        tmp1.insert(0, boards[y])
        tmp_board = list(itertools.chain(*tmp1))
        #print("Get format 1 :", tmp_board[-1], tmp_board)
        num = tmp_board[0]

        if len(LastQ) >= y:
            LastQ.pop(y - 1)
            LastQ.insert(y - 1, num)
        else:
            LastQ.insert(y - 1, num)

        tmp_board.remove(tmp_board[0])
        del boards[y]
        for r in tmp_board:
            boards[y].append(r)
        #print("Get format 2 :", boards[y])

            # Create next board (y + 1) - deleting blocked cells
        #print("Check 2.1: y + 1 > N_ ", y + 1 > N_, ", nkey = y, ELSE, nkey = y + 1")
        if y + 1 > N_:
            nKey = y
        else:
            nKey = y + 1
        #print("Check 2.2: nKey ", nKey)
        r = 0

        def blockcells(num):
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
            #print("Diagonais para direita/abaixo", line)

            l = int(cel[0])
            c = int(cel[1])
            if c > 1:  # Diagonais para direita/acima
                while c >= 1 and l >= 1:
                    cell = str(l) + "." + str(c)
                    line.insert(0, cell)
                    l = l - 1
                    c = c + 1
            #print("Diagonais para direita/acima", line)

            l = int(cel[0])
            c = int(cel[1])
            if c > 1:  # Diagonais para esquerda/acima   GOOD
                while c >= 1 and l >= 1:
                    cell = str(l) + "." + str(c)
                    line.insert(0, cell)
                    l = l - 1
                    c = c - 1
            #print("Diagonais para esquerda/acima", line)

            l = int(cel[0])
            c = int(cel[1])
            if l < N_ and c > 1:  # Diagonais para esquerda/abaixo  GOOD
                while l <= N_ and c >= 1:
                    cell = str(l) + "." + str(c)
                    line.append(cell)
                    l = l + 1
                    c = c - 1
            #print("Diagonais para esquerda/abaixo", line)

            l = int(cel[0])
            c = int(cel[1])
            if c > 1:  # Horizontal para a esquerda
                while c >= 1:
                    cell = str(l) + "." + str(c)
                    line.insert(0, cell)
                    c = c - 1
            #print("Horizontal para a esquerda", line)

            l = int(cel[0])
            c = int(cel[1])
            if c < N_:  # Horizontal para a direita
                while c <= N_:
                    cell = str(l) + "." + str(c)
                    line.append(cell)
                    c = c + 1
            #print("Horizontal para a direita", line)

            l = int(cel[0])
            c = int(cel[1])
            if l > 1:  # Vertical para cima
                while l >= 1:
                    cell = str(l) + "." + str(c)
                    line.append(cell)
                    l = l - 1
            #print("Vertical para cima", line)

            l = int(cel[0])
            c = int(cel[1])
            if l < N_:  # Vertical para cima
                while l <= N_:
                    cell = str(l) + "." + str(c)
                    line.append(cell)
                    l = l + 1
            #print("Vertical para baixo", line)
            #print("Get next_board 2 :", line)
            #sys.exit(0)
            for r in line:
                if r in tmp_board:
                    tmp_board.remove(r)

        #print("tmp_board - before", tmp_board)
        blockcells(num)
        #print("tmp_board - after", tmp_board)

        #print("Check 2.3: len(boards[nKey]) != 0", len(boards[nKey]) != 0, "del board[nkey")
        if len(boards[nKey]) != 0:
            del boards[nKey]
        for r in tmp_board:
            boards[nKey].append(r)
        #print("Next board", nKey, boards[nKey])
        #print("Check 2.4:", (nKey == N_ and len(boards[nKey]) > 0), "Check 5")
        if nKey == N_ and len(boards[nKey]) > 0:
            #print("Check 2.5: len(LastQ) == nKey", len(LastQ) == nKey, "pop")
            if len(LastQ) == nKey:
                LastQ.pop(nKey - 1)
            tmp1.insert(0, boards[nKey])
            tmp_board = list(itertools.chain(*tmp1))
            num = tmp_board[0]
            LastQ.insert(nKey, num)
            with open("myboard-"+str(N_)+"x"+str(N_)+"-"+timex+".txt", 'at') as f:
                for r in LastQ:
                    f.write(r + ";")
                f.write("\n")
            with open("myboard-"+str(N_)+"x"+str(N_)+"-"+timex+".txt", "rt") as f:
                t = len(f.readlines())
            #print("Last Board:", N_, LastQ)
            print(N_, " Board 1 size:", len(boards[1]), "Board 3 size:", len(boards[3]))
    def getmillioprize():
        i = 1
        while True:
            while len(boards[i]) > (N_ - i + 1):
                #print(i)
                #print("Check 1.0: len(boards[",i,"]) > (N_ - i + 1)", len(boards[i]) > (N_ - i + 1))
                #print("1 - len(boards[", i, "]", len(boards[i]))
                check_board(i)
                i = i + 1
                #print("Check 1.1:",i,"==N_", i == N_)
                if i == N_:
                    #print("Last board: ", N_, boards[N_])
                    False
            #print("Check 1.2:", i,"-1 < 1", i - 1 < 1,"i = 1, ELSE i = i - 1")
            if i - 1 < 1 and len(boards[1]) >= N_:
                i = 1
            if i - 1 < 1 and len(boards[1]) < N_:
                print("Exiting:", i - 1, len(boards[1]))
                break
                #sys.exit(0)
            else:
                i = i - 1


    sair = 0
    createboard()
    getmillioprize()