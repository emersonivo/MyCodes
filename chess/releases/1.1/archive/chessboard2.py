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
            if x ==1 and y == 1:
                lastx = len(rangelin) + 1
                lasty = len(rangecol) + 1
                last = int(str(lastx) + str(lasty))
                for p in range(11, last, 11):
                    d['Diag%02d' % int(lincol)].append(p)
                    #print(p)
            elif x > 1 and y == 1:
                beg = str(x) + str(y)
                fin = str(y) + str(x)
                for p in range(int(beg), int(fin)-1, -9):
                    d['Diag%02d' % int(lincol)].append(p)
                    #print(p)
            elif x == 1 and y > 1:      # From Colunm 1 to Line 1
                beg = str(x) + str(y)
                fin = str(y) + str(x)
                for p in range(int(beg), int(fin)+1, +9):
                    d['Diag%02d' % int(lincol)].append(p)
                    #print(p)
            elif x >= 1 and y == 8:
                beg = str(x) + str(y)
                fin = str(y) + str(x)
                for p in range(int(beg), int(fin) + 1, +9):
                    d['Diag%02d' % int(lincol)].append(p)
                    #print(p)
            elif x == 8 and y >= 1:
                beg = str(x) + str(y)
                fin = str(y) + str(x)
                for p in range(int(beg), int(fin), -11):
                    d['Diag%02d' % int(lincol)].append(p)
    print(d['Diag28'])



    #print(Diag21)



diagonais()