import re
class Book:
    class _blank:
        class Part_II:
            def Chapter_4():
                def _Dict(): #Page 166/1594
                    Dict1 = {'a' : '1', 'b' : '2', 'c': '3'}
                    Dict2 = dict(d='4', e='5', f='6')
                    print('Dict1:', Dict1)
                    print('Dict2:', Dict2)
                def _Set(): #Page 178/1594
                    Set1 = set('123415671890')
                    Set2 = set('abcdbcdecdefdefg')
                    print("Set1:", Set1, "Set2:", Set2)
                    for l in Set2:
                        Set1.add(l)
                    print(Set1)
                def _Object(): #Page 180/1594
                    _Set = set('123415671890')
                    _MyDict = dict(a='1', b='2')
                    print(type(_Set))
                    print(type(_MyDict))
                #_Dict()
                #_Set()
                #_Object()                    
            def Chapter_5():
                def _Math(): #Page 207/1594
                    print("sum: ", sum((1, 2, 3, 4)))
                    print("sum2: ", (1 + 3))
                    print("Min: ", min(3, 5, 1, 9), "Max: ", max(3, 5, 1, 9))
                _Math()
            def Chapter_6():
                def Vars1():
                    a = 3
                    b = a
                    print "#1 a", a, "b", b
                    a = 5
                    print "#2 a", a, "b", b
                def Vars2():
                    L1 = [2, 4, 6]
                    L2 = L1
                    print "L1: ", L1, "| L2: ", L2
                    L1[0] = 24
                    print "L1: ", L1, "| L2: ", L2
                #Vars1
                Vars2()
            def Chapter_7():
                #Page 243/1594
                MyString = "Salve o Tricolor Paulista, Amado Time Brasileiro"
                R = MyString.rstrip()
                print "#1 - Find:", MyString.find("Tricolor")
                print "           ", MyString
                print "#2 - rstrip", R, "Didn't work"
                print "#3 - replace: ", MyString.replace('Time', 'Clube')
                print "#4 - split: ", MyString.split(',')
                print "#5 - lower: ", MyString.lower()
                print "#6 - endeith: ", MyString.endswith(" VAMOS SAO PAULO")
                print "#7 - join: ", ','.join('string1 string2')
                print "#8 - encode:", MyString.encode('latin-1')
                MyShort = "Tricolor"
                for x in MyShort: print "#9 - iteration: ", x
                print "#10 - iteration: ", 'Tricolor' in MyString
                print "#11 - map; ", map(ord, MyShort)
                print "#12 - match: ", re.match('Tri(.*)or', MyString)
                print "#13 - match: ", re.match('Tri(.*)or', MyShort) #Page 244/1594

            #Chapter_4()
            #Chapter_5()
            #Chapter_6()
            Chapter_7()

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

Book._blank.Part_II
#Book._Worker