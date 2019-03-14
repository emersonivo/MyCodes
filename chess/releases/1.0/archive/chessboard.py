def diagonais():
    from collections import defaultdict
    d = globals()
    import pprint
    rangelin = range(1,9)
    rangecol = range(1,9)
    for x in rangelin:
        for y in rangecol:
            lincol = str(x)+str(y)
            d['Diag%02d' % int(lincol)] = []

    for x in rangelin:
        for y in rangecol:
            lincol = str(x) + str(y)
            if x ==1 and y == 1:        # Diagonal 11 > 88
                lastx = len(rangelin) + 1
                lasty = len(rangecol) + 1
                last = int(str(lastx) + str(lasty))
                for p in range(11, last, 11):
                    d['Diag%02d' % int(lincol)].append(p)
                    #print(p)
            elif x > 1 and y == 1:      # Diagonal 21 > 12
                beg = str(x) + str(y)
                fin = str(y) + str(x)
                for p in range(int(beg), int(fin)-1, -9):
                    d['Diag%02d' % int(lincol)].append(p)
                    #print(p)
            elif x == 1 and y > 1:      # Diagonal 12 > 23
                beg = str(x) + str(y)
                fin = str(y) + str(x)
                for p in range(int(beg), int(fin)+1, +9):
                    d['Diag%02d' % int(lincol)].append(p)
                    #print(p)
            elif x >= 1 and y == 8:     # Diagonal 18 > 27
                beg = str(x) + str(y)
                fin = str(y) + str(x)
                for p in range(int(beg), int(fin) + 1, +9):
                    d['Diag%02d' % int(lincol)].append(p)
                    #print(p)
            elif x == 8 and y >= 1:     # Diagonal 82 > 71
                beg = str(x) + str(y)
                fin = str(y) + str(x)
                for p in range(int(beg), int(fin), -11):
                    d['Diag%02d' % int(lincol)].append(p)
                    #print(p)
    print(d['Diag28'])



    #print(Diag21)



diagonais()