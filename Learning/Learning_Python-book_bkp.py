import re
import os
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
                    print "#C6.1 a", a, "b", b
                    a = 5
                    print "#C6.2 a", a, "b", b
                def Vars2():
                    L1 = [2, 4, 6]
                    L2 = L1
                    print "#C6.3 L1: ", L1, "| L2: ", L2
                    L1[0] = 24
                    print "#C6.4 L1: ", L1, "| L2: ", L2
                Vars1()
                Vars2()
            def Chapter_7():
                #Page 243/1594
                MyString = "Salve o Tricolor Paulista, Amado Time Brasileiro"
                R = MyString.rstrip()
                print "#C7.1 - Find:", MyString.find("Tricolor")
                print "           ", MyString
                print "#C7.2 - rstrip", R, "Didn't work"
                print "#C7.3 - replace: ", MyString.replace('Time', 'Clube')
                print "#C7.4 - split: ", MyString.split(',')
                print "#C7.5 - lower: ", MyString.lower()
                print "#C7.6 - endeith: ", MyString.endswith(" VAMOS SAO PAULO")
                print "#C7.7 - join: ", ','.join('string1 string2')
                print "#C7.8 - encode:", MyString.encode('latin-1')
                MyShort = "Salve o Tricolor"
                for x in MyShort: print "#9 - iteration: ", x
                print "#C7.9 - iteration: ", 'Tricolor' in MyString
                print "#C7.10 - map; ", map(ord, MyShort)
                print "#C7.11 - match: ", re.match('Tri(.*)or', MyShort) #Do not Work
                print "#C7.12 - match: ", re.match('Tri(.*)or', MyShort) #Do not work
                MyLong = """
                This is the first line
                And this is the second"""
                print "#C7.13 - MyLong", MyLong
                print("#C7.14", "-" * 15)
                #for c in MyShort: print("#C7.15 :", c, end='') Do not work
                print "#C7.16 - Slicing :", MyShort[1:16:2]
                print "#C7.17 - Slicing :", MyShort[::2]
                print "#C7.18 - Slicing :", MyShort[::-1]
                print "#C7.19 - Changing string: %d %s" % (25, 'March')
                print "#C7.20 - Look at page {0}/{1} for {2} references".format(262, 1594, 'Method of Strings')
                print "#C7.21 - Method lower", MyShort.lower()
                print "#C7.22 - split", MyShort.split()
                x = 10
                print "#C7.23 - Advanced Formatting - Page 271/1594 #a:%d, #b:%-6d, #c:%06d." % (x, x, x) 

                template = '{0}, {1} and {2}'
                print "#C7.24 - Formatting Method", template.format('spam', 'ham', 'eggs')
                template = '{key1}, {key2} and {key3}'
                print "#C7.25 - Formatting Method", template.format(key1='bla', key2='ble', key3='bli')
                template = '{}, {} and {}'
                print "#C7.26 - Formatting Method", template.format('spam', 'ham', 'eggs')
                template = '%s, %s and %s'
                print "#C7.27 - Formatting Method", template % ('spam', 'ham', 'eggs')
                # ------------- page 276/1594 ---------------
                import sys
                print '#C7.28 My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'})
                print '#C7.29 My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'})
                somelist = list('SPAM')
                print '#C7.30: ', somelist
                print '#C7.31 first={0[0]}, third={0[2]}'.format(somelist)
            def Chapter_8():
                MyList = []
                MyList = ['abc', 'def', 'ghi', ['jkl', 'mno', 'pqr']]
                print '#C8.1 MyList: ', MyList[0][2], MyList[3][0][1]
                print '#C8.2 Mylist * 2', MyList * 2
                MyList.append('stu')
                print '#C8.3 MyList.append: ', MyList
                MyList.extend(['vxy'])
                print '#C8.4 MyList.extend: ', MyList
                MyList.insert(0, 'wz')
                print '#C8.5 MyList.insert: ', MyList
                print '#C8.6 MyList.pop: ', MyList.pop(1)
                
                #for x in [1, 2, 3]: print '#C8.7 x', x, end=' '
                rep = [ x * 4 for x in 'SPAM']; print '#C8.8 rep: ', rep
                matrix = [[1,2,3],
                [4,5,6],
                [7,8,9]]
                print '#C8.9 Matrix: ', matrix
                print '#C8.10 Matrix [2,2]', matrix[2][2]

                matrix[0][0] = 'a'
                print '#C8.11 matrix[0][0] = a: ', matrix
            def Chapter_9():
                def Tuples():
                    MyTuple = ('a', 'b', 'c')
                    print '#C9.1 MyTuple[0]', MyTuple[0]
                    MyTuple = ('abc', 'def', 'ghi')
                    print '#C9.2 MyTuple[1][0]', MyTuple[1][0]
                    MyTuple = tuple('SPAM')
                    print '#C9.3 MyTuple', MyTuple
                    print '#C9.4 len(MyTuple)', len(MyTuple)
                    print '#C9.5 MyTuple * 3', MyTuple * 3
                    t1 = ('c9')
                    t2 = 'c9'
                    t3 = ('c9',)
                    t4 = 'c9',
                    print '#C9.6 Types Tuples: ', type(t1), type(t2), type(t3), type(t4)
                    L = list(MyTuple)
                    print '#C9.7 List of Tuple: ', L
                    L[0] = 'R'
                    print '#C9.8 Replace list item', L
                    T = tuple(L)
                    print '#C9.9 Tuple of list: ', T
                    print '#C9.10 Sorting tuple:', sorted(T)
                def Files():
                    input = open(homedir+'/Learning/file_c9.txt')
                    # aString = input.read()
                    # print '#C9.11 - Read file into a string', aString
                    # aString = input.readline()
                    # print '#C9.12 - Read file into a string', aString
                    # aList = input.readlines()
                    # print '#C9.13 - Read file into a list', aList
                    # with open(homedir+"/Learning/file2_c9.txt", 'w+') as output:
                    #     for x in range(1, 5):
                    #         output.writelines('Line'+str(x)+'\n')
                    # MyString = 'abcd   '
                    # print "C9.14: ", len(MyString), MyString
                    # print "C9.15: ", len(MyString.rsplit()), MyString.rsplit()
                    # MyString = '    abcd'
                    # print "C9.16: ", len(MyString), MyString
                    # print "C9.17: ", len(MyString.rsplit()), MyString.rsplit()
                    #------------------------
                    # MyDict = {'abobora': 'legumes', 'banana': 'fruta', 'cascalho': 'rocha'}
                    # F = open(homedir+'/Learning/filedict_c9.dump', 'wb')
                    # import pickle
                    # pickle.dump(MyDict, F)
                    # F.close()
                    #------------------------
                    # F2 = open(homedir+'/Learning/filedict_c9.dump', 'rb')
                    # MyRestoredDict = pickle.load(F2)
                    # print '#C9.18 MyDict: ', MyDict
                    # print '#C9.19 MyRestoredDict: ', MyRestoredDict
                    #------------------------
                    # vars1 = dict(a1=1, b1=2, c1=3)
                    # vars2 = dict(a2=2, b2=2, c2=2)
                    # vars3 = dict(a3=3, b3=3, c3=3)
                    # MyDict = dict(L1=vars1, L2=vars2, L3=vars3)
                    # print "#C9.20 MyDict: ", MyDict
                    # import json
                    # F3 = open(homedir+'/Learning/filedict_c9.json', 'wb')
                    # json.dump(MyDict, F3, indent=4)
                    # F3.close()
                    # print ("#C9.21 print + open: ", open(homedir+'/Learning/filedict_c9.json').read())
                    # F4 = open(homedir+'/Learning/filedict_c9.json', 'rb')
                    # MyRestoredDict = json.load(F4)
                    # print '#C9.21 MyDict: ', MyDict
                    # print '#C9.2 MyRestoredDict: ', MyRestoredDict
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
            Chapter_10()
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

#Book._blank.Part_II
Book._blank.Part_III
#Book._Worker