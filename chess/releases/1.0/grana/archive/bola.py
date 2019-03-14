def diagonais():
    from collections import defaultdict
    d = globals()
    import pprint
    x = 8
    y = 8
    rangelin = range(1,x + 1)
    rangecol = range(1,y + 1)
    linx = 1
    colx = 1
    for linx < x:
        for colx < y:
            lincol = str(lin)+str(col)
            d['Diag%02d' % int(lincol)] = []
            lin+=1
            col+=1

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
                    print(p)



    #print(Diag21)



diagonais()