#!/usr/bin/python3.6
import re
import os
import sys
homedir = os.getcwd()
class Book:
    class _blank:
        class Part_II:
            def Chapter_4():
                def _Dict(): #Page 166/1594
                    Dict1 = {'a' : '1', 'b' : '2', 'c': '3'}
                    Dict2 = dict(d='4', e='5', f='6')
                    print('#C4.1 Dict1:', Dict1)
                    print('#C4.2 Dict2:', Dict2)
                def _Set(): #Page 178/1594
                    Set1 = set('123415671890')
                    Set2 = set('abcdbcdecdefdefg')
                    print("#C4.3 Set1:", Set1, "Set2:", Set2)
                    for l in Set2:
                        Set1.add(l)
                    print('#C4.4: ', Set1)
                def _Object(): #Page 180/1594
                    _Set = set('123415671890')
                    _MyDict = dict(a='1', b='2')
                    print('#C4.5: ', type(_Set))
                    print('#C4.6: ', type(_MyDict))
                _Dict()
                _Set()
                _Object()                    
            def Chapter_5():
                def _Math(): #Page 207/1594
                    print("#C5.1 sum: ", sum((1, 2, 3, 4)))
                    print("#C5.2 sum2: ", (1 + 3))
                    print("#C5.3 Min: ", min(3, 5, 1, 9), "Max: ", max(3, 5, 1, 9))
                _Math()
            def Chapter_6():
                def Vars1():
                    a = 3
                    b = a
                    print ("#C6.1 a", a, "b", b)
                    a = 5
                    print ("#C6.2 a", a, "b", b)
                def Vars2():
                    L1 = [2, 4, 6]
                    L2 = L1
                    print ("#C6.3 L1: ", L1, "| L2: ", L2)
                    L1[0] = 24
                    print ("#C6.4 L1: ", L1, "| L2: ", L2)
                Vars1()
                Vars2()
            def Chapter_7():
                #Page 243/1594
                MyString = "Salve o Tricolor Paulista, Amado Time Brasileiro"
                R = MyString.rstrip()
                print ("#C7.1 - Find:", MyString.find("Tricolor"))
                print ("           ", MyString)
                print ("#C7.2 - rstrip", R, "Didn't work")
                print ("#C7.3 - replace: ", MyString.replace('Time', 'Clube'))
                print ("#C7.4 - split: ", MyString.split(','))
                print ("#C7.5 - lower: ", MyString.lower())
                print ("#C7.6 - endeith: ", MyString.endswith(" VAMOS SAO PAULO"))
                print ("#C7.7 - join: ", ','.join('string1 string2'))
                print ("#C7.8 - encode:", MyString.encode('latin-1'))
                MyShort = "Salve o Tricolor"
                for x in MyShort: print ("#9 - iteration: ", x)

                print ("#C7.9 - iteration: ", 'Tricolor' in MyString)
                print ("#C7.10 - map; ", map(ord, MyShort))
                print ("#C7.11 - match: ", re.match('Tri(.*)or', MyShort)) #Do not Work
                print ("#C7.12 - match: ", re.match('Tri(.*)or', MyShort)) #Do not work
                MyLong = """
                This is the first line
                And this is the second"""
                print ("#C7.13 - MyLong", MyLong)
                print ("#C7.14", "-" * 15)
                #for c in MyShort: print("#C7.15 :", c, end='') Do not work
                print ("#C7.16 - Slicing :", MyShort[1:16:2])
                print ("#C7.17 - Slicing :", MyShort[::2])
                print ("#C7.18 - Slicing :", MyShort[::-1])
                print ("#C7.19 - Changing string: %d %s" % (25, 'March'))
                print ("#C7.20 - Look at page {0}/{1} for {2} references".format(262, 1594, 'Method of Strings'))
                print ("#C7.21 - Method lower", MyShort.lower())
                print ("#C7.22 - split", MyShort.split())
                x = 10
                print ("#C7.23 - Advanced Formatting - Page 271/1594 #a:%d, #b:%-6d, #c:%06d." % (x, x, x))

                template = '{0}, {1} and {2}'
                print ("#C7.24 - Formatting Method", template.format('spam', 'ham', 'eggs'))
                template = '{key1}, {key2} and {key3}'
                print ("#C7.25 - Formatting Method", template.format(key1='bla', key2='ble', key3='bli'))
                template = '{}, {} and {}'
                print ("#C7.26 - Formatting Method", template.format('spam', 'ham', 'eggs'))
                template = '%s, %s and %s'
                print ("#C7.27 - Formatting Method", template % ('spam', 'ham', 'eggs'))
                # ------------- page 276/1594 ---------------
                import sys
                print ('#C7.28 My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))
                print ('#C7.29 My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'}))
                somelist = list('SPAM')
                print ('#C7.30: ', somelist)
                print ('#C7.31 first={0[0]}, third={0[2]}'.format(somelist))
            def Chapter_8():
                MyList = []
                MyList = ['abc', 'def', 'ghi', ['jkl', 'mno', 'pqr']]
                print ('#C8.1 MyList: ', MyList[0][2], MyList[3][0][1])
                print ('#C8.2 Mylist * 2', MyList * 2)
                MyList.append('stu')
                print ('#C8.3 MyList.append: ', MyList)
                MyList.extend(['vxy'])
                print ('#C8.4 MyList.extend: ', MyList)
                MyList.insert(0, 'wz')
                print ('#C8.5 MyList.insert: ', MyList)
                print ('#C8.6 MyList.pop: ', MyList.pop(1))
                
                #for x in [1, 2, 3]: print ('#C8.7 x', x, end=' '
                rep = [ x * 4 for x in 'SPAM']; print ('#C8.8 rep: ', rep)
                matrix = [[1,2,3],
                [4,5,6],
                [7,8,9]]
                print ('#C8.9 Matrix: ', matrix)
                print ('#C8.10 Matrix [2,2]', matrix[2][2])

                matrix[0][0] = 'a'
                print ('#C8.11 matrix[0][0] = a: ', matrix)
            def Chapter_9():
                def Tuples():
                    MyTuple = ('a', 'b', 'c')
                    print ('#C9.1 MyTuple[0]', MyTuple[0])
                    MyTuple = ('abc', 'def', 'ghi')
                    print ('#C9.2 MyTuple[1][0]', MyTuple[1][0])
                    MyTuple = tuple('SPAM')
                    print ('#C9.3 MyTuple', MyTuple)
                    print ('#C9.4 len(MyTuple)', len(MyTuple))
                    print ('#C9.5 MyTuple * 3', MyTuple * 3)
                    t1 = ('c9')
                    t2 = 'c9'
                    t3 = ('c9',)
                    t4 = 'c9',
                    print ('#C9.6 Types Tuples: ', type(t1), type(t2), type(t3), type(t4))
                    L = list(MyTuple)
                    print ('#C9.7 List of Tuple: ', L)
                    L[0] = 'R'
                    print ('#C9.8 Replace list item', L)
                    T = tuple(L)
                    print ('#C9.9 Tuple of list: ', T)
                    print ('#C9.10 Sorting tuple:', sorted(T))
                def Files():
                    input = open(homedir+'/Learning/file_c9.txt')
                    # aString = input.read()
                    # print ('#C9.11 - Read file into a string', aString
                    # aString = input.readline()
                    # print ('#C9.12 - Read file into a string', aString
                    # aList = input.readlines()
                    # print ('#C9.13 - Read file into a list', aList
                    # with open(homedir+"/Learning/file2_c9.txt", 'w+') as output:
                    #     for x in range(1, 5):
                    #         output.writelines('Line'+str(x)+'\n')
                    # MyString = 'abcd   '
                    # print ("C9.14: ", len(MyString), MyString
                    # print ("C9.15: ", len(MyString.rsplit()), MyString.rsplit()
                    # MyString = '    abcd'
                    # print ("C9.16: ", len(MyString), MyString
                    # print ("C9.17: ", len(MyString.rsplit()), MyString.rsplit()
                    #------------------------
                    # MyDict = {'abobora': 'legumes', 'banana': 'fruta', 'cascalho': 'rocha'}
                    # F = open(homedir+'/Learning/filedict_c9.dump', 'wb')
                    # import pickle
                    # pickle.dump(MyDict, F)
                    # F.close()
                    #------------------------
                    # F2 = open(homedir+'/Learning/filedict_c9.dump', 'rb')
                    # MyRestoredDict = pickle.load(F2)
                    # print ('#C9.18 MyDict: ', MyDict
                    # print ('#C9.19 MyRestoredDict: ', MyRestoredDict
                    #------------------------
                    # vars1 = dict(a1=1, b1=2, c1=3)
                    # vars2 = dict(a2=2, b2=2, c2=2)
                    # vars3 = dict(a3=3, b3=3, c3=3)
                    # MyDict = dict(L1=vars1, L2=vars2, L3=vars3)
                    # print ("#C9.20 MyDict: ", MyDict
                    # import json
                    # F3 = open(homedir+'/Learning/filedict_c9.json', 'wb')
                    # json.dump(MyDict, F3, indent=4)
                    # F3.close()
                    # print ("#C9.21 print + open: ", open(homedir+'/Learning/filedict_c9.json').read())
                    # F4 = open(homedir+'/Learning/filedict_c9.json', 'rb')
                    # MyRestoredDict = json.load(F4)
                    # print ('#C9.21 MyDict: ', MyDict
                    # print ('#C9.2 MyRestoredDict: ', MyRestoredDict
                #Tuples
                Files() #Page 344/1594
            #Chapter_4()
            #Chapter_5()
            #Chapter_6()
            #Chapter_7()
            #Chapter_8()
            #Chapter_9() #Page 328/1594
        class Part_III:
            def Chapter_10():
                x = 0
                y = 1
                w = 3
                if (x < y and
                    y < w and
                    w > x):
                    print ("#C10.1 \
                    \nif (x < y and \
                        \n\ty < w and \
                        \n\tw < x):")

                while True:
                    reply = input("#C10.2 - Enter text:")
                    if reply == 'stop': break
                    print(reply.upper())

                while True:
                    reply = input('Enter text: ')
                    if reply == 'stop': break
                    try:
                        num = int(reply)
                    except:
                        print('Bad!' * 8)
                    else:
                        print(num ** 2)
                print("Bye")
            def Chapter_11():
                seq = [1, 2, 3, 4]
                a, b, c, d = seq
                print("#C11.1 ", a, b, d)
                # a, b = seq Expected fail
                a, *b = seq
                print("#C11.2 ", a, b)
                a, *b, c = seq
                print("#C11.3 ", a, b, c)
                for (a, b, c) in [(1, 2, 3),('a', 'b','c'),(7, 8, 9)]:
                    print("#C11.4 a="+str(a), " b="+str(b), " c="+str(c))
                a = b = []
                b.append(42)
                print("C#11.5 ", a, b)

                x = 1
                x += 3
                print("#C11.6 ", x)
                L = [1, 2]
                L = L + [3]
                print("#C11.7 Adding element to a list L = L + [3]:", L)
                L.append(4)
                print("#C11.8 Adding element to a list L.append(4):", L)
                L.extend([5, 6])
                print("#C11.9 Adding element to a list L.extend([5, 6]):", L)
                L += [8, 9, 10]
                print("#C11.9 Adding element to a list L += [8, 9, 10]:", L)
                seq = [1, 2, 3, 4]
                a, b, c, d = seq
                
                print("#C11.10 Printing direct to file: ", a, b, d, sep='@', end='END\n', file=open(homedir+'/page413_1594', 'w+'))
                
                print("#C11.11 Using print to read from file:", open(homedir+'/page413_1594').read())
            def Chapter_12():
                # branch = {'spam': 1.25, 'ham': 1.99, 'eggs': 0.99}
                # print('#C12.1 ', branch.get('spam', 'Bad choice'))
                # print(branch)
                # opt = input("Make your choice: ")
                # print('#C12.2 ', branch.get(opt, 'Bad choice'))
                Y = 3; Z = 9
                X = input("Enter X value: ")
                A = Y if X else Z
                print("#C12.3 Page 435/1594: ", A)
            def Chapter_13():
                opt = 10
                while True:
                    print("C13.1 Block of three whiles to test 'break', 'continue' and 'loop'")
                    while True:
                        print("Second while")
                        while True:
                            print("Third while")
                            opt = input("Enter 9 to exit: ")
                            if int(opt) == 9:
                                print("while #3 - opt == 9 - break")
                                break
                            elif int(opt) < 4:
                                print("while #3 - opt < 4 - break")
                                break
                            elif int(opt) > 3 and int(opt) < 6:
                                print('continue')
                                continue
                            else:
                                print("else - We continue here in the third loop")
                        if int(opt) == 9: 
                            print("while #2 - opt == 9 - break")
                            break
                        else:
                            print("while #2 - opt != 9 - continue")
                            #continue
                    if int(opt) == 9: 
                        print("while #1 - opt == 9 - break")
                        break
            def Chapter_14():
                L = [1, 4, 7]
                I = iter(L)
                while True:
                    try:
                        x = next(I)
                    except StopIteration:
                        break
                    print('#C14.1', x ** 2, end='%\n')
                for I in L:
                    print('#C14.2', I ** 2, end='@\n')

                P = os.popen('dir')
                for I in P:
                    print('#C14.3', I, end=';\n')
                
                L = [ x + 10 for x in L]
                print('#C14.4 - L = [ x + 10 for x in L]\n', L,'\n')

                L = [ x + 10 for x in L if x > 13]
                print('#C14.5 - L = [ x + 10 for x in L if x > 13]\n', L,'\n')

                L = [ x + y for x in 'abc' for y in 'xyz' ]
                print("#C14.6 L = [ x + y for x in 'abc' for y in 'xyz' ]\n", L,'\n')

                L2 = list(zip('abc', 'xyz'))
                print("#C14.7 L2 = list(zip('abc', 'xyz'))\n", L2,'\n')

                D = {x: y for x, y in enumerate('abcdefg')}
                print("#C14.8 - D = {x: y for x, y in enumerate('abcdefg')}\n", D,'\n')

                D = {'a': 1, 'b': '', 'c': 3}
                print("#C14.9 - D = ", D)
                print("#C14.10 any(D)", any(D))
                print("#C14.11 all(D)", all(D),'\n')

                L = ['a', 'b', '', 'd']
                print("#C14.12 - L = ", L)
                print("#C14.13 any(L)", any(L))
                print("#C14.14 all(L)", all(L),'\n')

                LR = list(range(10))
                print("#C14.15 LR = list(range(10)) ", LR, '\n')

                D = {'a': 1, 'b': 2, 'c': 3}
                k = D.keys()
                print("#C14.16 - k = D.keys()", k)
                print("#C14.17 - list(k))",list(k)) 

                v = D.values()
                print("#C14.18 - v = D.values()", v)
                print("#C14.19 - list(v))",list(v)) 
                print("#C14.20 - list(D.items())",list(D.items()))
            
            # Chapter_10()
            # Chapter_11()
            # Chapter_12()
            # Chapter_13()
            # Chapter_14()
        class Part_IV:
            def Chapter_16():
                def maker(x):
                    print(x)
                    def action(y):
                        print(y)
                        return x ** y
                    return action(x)
                #f = maker(3)
                #print(f)
            def Chapter_17():
                x = 99
                def f2():
                    print(x)
                #f2()
                
                def tester(start):
                    global state
                    state = start
                    def nested(label):
                        #nonlocal state
                        global state
                        print("#C17.1 - nonlocal statement ", label, state)
                        state += 1
                    return nested

                F = tester(0)
                for x in ['spam', 'eggs', 'ham']:
                    F(x)

                class tester2:
                    def __init__(self, start):
                        self.state = start
                    def nested(self, label):
                        print("C#17.2 simple class: ", label, self.state)
                        self.state += 1
                
                F = tester2(0)
                for x in ['boll', 'car', 'house']:
                    F.nested(x)

                class tester3:
                    def __init__(self, start):
                        self.state = start
                    def __call__(self, label):
                        print("C#17.3 called class: ", label, self.state)
                        self.state += 1
                    def nested(self, label):
                        print("C#17.4 nested + called class: ", label, self.state)
                        self.state += 3

                F = tester3(0)
                for x in ['cat', 'dog', 'horse']:
                    F(x)
                    F.nested(x)
            def Chapter_18():
                def changer(a, b):
                    a = 2
                    b[0] = 'spam'
                    return a, b
                
                X = 1
                L = [1, 2]
                #print("#C18.1 ", changer(X, L))

                def multiplex(x, y):
                    x = 2
                    y = [3, 4]
                    return x, y
                
                X = 1
                L = [1, 2]
                X, L = multiplex(X, L)
                print("#C18.2 ", X, L)
            def Chapter_19():
                def mysum(L):
                    if not L:
                        return 0
                    else:
                        return L[0] + mysum(L[1:])
                print("#C19.1 page 608/1594 - sum 1 ", mysum([1, 2, 3, 4, 5]))
                def mysum2(L):
                    return 0 if not L else L[0] + mysum2(L[1:])
                print("#C19.2 page 608/1594 - sum 2 ", mysum2([1, 2, 3, 4, 5]))
                def mysum3():
                    L = [1, 2, 3, 4, 5]
                    sum = 0
                    while L:
                        sum += L[0]
                        L = L[1:]
                    return sum
                print("#C19.3 page 610/1594 - sum 3 ", mysum3())
                def mysum4():
                    L = [1, 2, 3, 4, 5]
                    sum = 0
                    for x in L: sum +=x
                    return sum                    
                print("#C19.4 page 610/1594 - sum 4 ", mysum4())
                def mysum5():
                    def sumtree(L):
                        tot = 0
                        for x in L:
                            #print("#1", x)
                            if not isinstance(x, list):
                                tot += x
                            else:
                                tot += sumtree(x)
                        return tot
                    L = [1, [2, [3, 4], 5], 6, [7, 8]]
                    return sumtree(L)
                print("#C19.5 - page 610/1594 ", mysum5())
                def mysum6():
                    def sumtree2(L):
                        tot = 0
                        items = list(L)
                        while items:
                            front = items.pop(0)
                            #print("#2 ", front)
                            if not isinstance(front, list):
                                tot += front
                            else:
                                items.extend(front)
                        return tot
                    L = [1, [2, [3, 4], 5], 6, [7, 8]]
                    return sumtree2(L)
                print("#C19.6 - page 611/1594 ", mysum6())                    
                def mysum7(a: 'spam', b: (1, 10), c: float) -> int:
                    return a + b + c
                print("#C19.7 - page 618/1594 ", mysum7(1, 2, 3))
                print("#C19.8 - page 618/1594 ", mysum7.__annotations__)
                for arg in mysum7.__annotations__:
                    print(arg, '=>', mysum7.__annotations__[arg])
                def func1(x, y, z): return x + y + z
                print("#C19.9 - page 620/1594 func def", func1(1, 2, 3))
                func2 = lambda x, y, z: x + y + z
                print("#C19.10 - page 623/1594 (lambda x, y, z: x + y + z) ")
                print(func2(1, 2, 3))
                lower = (lambda x, y: x if x < y else y)
                print("#C19.11 - page 623/1594 (lambda x, y: x if x < y else y) ")
                print(lower('aa', 'ab'))
                counters = [1, 2, 3, 4]
                def inc(x): return x + 10
                print("couters", counters)
                print("#C19.12 - page 626/1594 (list(map(inc, counters))")
                print(list(map(inc, counters)))
                print("#C19.13 - page 627/1594 (list(map((lambda x: x + 3), counters))")
                print(list(map((lambda x: x + 3), counters)))
                print("#C19.14 - page 628/1594 (list(filter((lambda x: x >0), range(-5, 5)))")
                print(list(filter((lambda x: x >0), range(-5, 5))))
                print("#C19.15 - page 628/1594 ([x for x in range(-5, 5) if x > 0]")
                print([x for x in range(-5, 5) if x > 0])
                from functools import reduce
                print("#C19.16 - page 629/1594 reduce((lambda x, y: x + y), [1, 2, 3, 4])")
                print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))
                import operator, functools
                print("#C19.17 - Page 629/1594 - functools.reduce(operator.add, [2, 4, 6]")
                print(functools.reduce(operator.add, [2, 4, 6]))
            def Chapter_20():
                print("C20.1 Page 634/1594 \nres = []\nfor x in 'spam' :\n\tres.append(ord(x))\n")
                print("C20.2 Page 634/1594 \nres = list(map(ord, 'spam'))")
                res = list(map(ord, 'spam'))
                print(res)     
                print("#C20.3 Page 634/1594 res = [ord(x) for x in 'hamburger']")
                res = [ord(x) for x in 'humburger']
                print(res)
                print("#C20.3 Page 635/1594 '[x for x in range(15) if x % 3 == 2]")
                print([x for x in range(15) if x % 3 == 2])
                print('Formal comprehension syntax\n[expression for target in itarable] OR\n \
                    [expression for target1 in iterable1 if condition1\n\
                                for target2 in iterable2 if condition2\n\
                                for targetN in iterableN if conditionN]')
                res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
                print("\n#C20.4 Page 636/1594 res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]")
                print(res)
                res = [(x, y, z) for x in range(10) if x % 2 == 0
                                 for y in range(10) if y % 3 == 1
                                 for z in range(10) if z % 5 == 3]
                print("\n#C20.5 Page 636/1594 res = [(x, y, z) for x in range(10) if x % 2 == 0\n \
                                 for y in range(10) if y % 3 == 1\n \
                                 for z in range(10) if z % 5 == 3]")
                print(res)
                print("\n#C20.6 Page 642/1594 L = [line.rstrip() for line in open('/data/git/MyCodes/Learning/file2_c9.txt')]")
                L = [line.rstrip() for line in open('/data/git/MyCodes/Learning/file2_c9.txt')]
                print(L)
                listoftuple = [('bob', 35, 'mgr'), ('sue', 40, 'dev')]
                print("\n#C20.7 Page 642/1594 A = [age for (name, age, job)in listoftuple]")
                A = [age for (name, age, job)in listoftuple]
                print(A)
                def gensquares(N):
                    for i in range(N):
                        yield i ** 2
                
                for i in gensquares(5):
                    print(i, end=' : ')
                print("\n\n#C20.8 Same result:")
                print("#20.8.1 [x ** 2 for x in range(4)]", [x ** 2 for x in range(4)])
                #X =  [x ** 2 for x in range(4)]
                L = list(x ** 2 for x in range(4))
                print("#C20.8.2 L = list(x ** 2 for x in range(4))", L)
                Line = "aaa bbb\nccc ddd\reee fff"
                print(Line)
                xLine = ''.join(x for x in Line.split() if len(x) > 1)
                print("#C20.9 ''.join(x for x in Line.split() if len(x) > 1)")
                print(xLine)
                def timesfour1(S): #Page 655/1594
                    for c in S:
                        yield c * 4
                G = timesfour1('spam')
                F = timesfour1('spam')
                print("#C20.10.1 As list" , list(G))
                print("#C20.10.2 As tuple", tuple(F))
                import os
                print("#C20.11 ... \nfor (root, subs, files) in os.walk('.'):\n\tfor name in files:\n\t\tif name.startswith('blibli'):\n\t\t\tprint(root, name)")
                for (root, subs, files) in os.walk('.'):
                    for name in files:
                        if name.startswith('blibli'):
                            print(root, name)
                
            # Chapter_16()
            # Chapter_17()
            # Chapter_18()
            # Chapter_19()
            Chapter_20() #653/1594
    class _Worker: #page 181/1594
        def __init__ (self, name, pay):
            self.name = name
            self.pay = pay
        def lastName(self):
            return self.name.split()[-1]
        def giveRaise(self, percent):
            self.pay *= (1.0 + percent)
        #emp1 = _Worker('Dunha Silva', 10000)
        #emp2 = _Worker('Ze Ruela', 24000)
        #print(emp1.lastName())
        #emp2.giveRaise(.10)
        #print(emp2.pay)

# Book._blank.Part_II
# Book._blank.Part_III
Book._blank.Part_IV
# Book._Worker