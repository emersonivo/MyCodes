# def prt1():
#     print("First Function")
#
# def prt2():
#     print("Second Function")
#
# for n in range(1,6):
#     for x in range(1,5):
#         y = n % x
#         if y != 0:
#             #print( str(n) + '%' + str(x) + "=" + str(y))
#             prt1()
#             continue
#         else:
#             #print(str(n) + '%%' + str(x) + "=" + str(y))
#             prt2()

#------------------------------------------------------------------
# total = 0
# def minhaconta(valor1, valor2):
#     #global total
#     total = valor1 * valor2
#     return total

# def printtotal():
#     newtotal = total
#     print(newtotal)

# conta1 = minhaconta(4,15)
# conta2 = minhaconta(3,27)
# print("conta1", conta1)
# print("conta2", conta2)

#-------------------------------------------------------------------
# def get_sex(sex='Undefined'):
#     if sex is "m":
#         print("Male")
#     elif sex is "f":
#         print("Female")
#     else:
#         print(sex)
#
# get_sex("m")
# get_sex("f")
# get_sex("x") #pesquisar como ignorar valor fora do contexto definido em 'if'
# get_sex()
#-------------------------------------------------------------------
# def keepfirst(first='Primeiro', second='Segundo', third='Terceiro'):
#     print(first, second, third)
#
# keepfirst()
# keepfirst(second='deuxieme')
# keepfirst(third='troisieme')
# -------------------------------------------------------------------
# def manyargs(*args):
#     total=0
#     for a in args:
#         total += a
#     print(total)
# manyargs(4)
# manyargs(6, 2, 9, 7)
# manyargs(34, 65, 87, 90, 23)
# -------------------------------------------------------------------
# def qualquercoisa(num1, num2, num3):
#     mynum = (num1 * 2) + (num2 * 3) + (num3 * 4)
#     print(mynum)
#
# first = [2, 3, 5]
# qualquercoisa(*first)
# -------------------------------------------------------------------
# list1 = {'a', 'b', 'c', 'd', 'b'}
# list2 = {'d', 'e', 'f', 'g'}
# print(list1)
# -------------------------------------------------------------------
# import eismod
# a = int(input("Give first num: "))
# b = int(input("Give the second num: "))
# eismod.mymod(a,b)
# -------------------------------------------------------------------
# import random
# list1=[]
# i = 1
# # for i in range(1,10):
# while i <= 10:
#     x = random.randrange(1,51)
#     if x not in list1:
#         list1.append(x)
#         print(i, "x not found ", x)
#         i = i + 1
#     else:
#         print(i, "x exist already ", x)
#
# print(list1)
# # -------------------------------------------------------------------
# fl1 = open('first_file.txt', 'w')
# fl1.write('This is the first line of my first file\n')
# fl1.write('This is the second line of my first file\n')
# fl1.close()
# # -------------------------------------------------------------------
# fl2 = open('first_file.txt', 'r')
# linex = fl2.read()
# print(linex)
# fl2.close()
# -------------------------------------------------------------------
# from urllib import request
# my_url = 'qualquer url para fazer download'
#
# def download_my_url(csv_url):
#     response = request.urlopen(csv_url)
#     csv = response.read()
#     csv_str = str(csv)
#     lines = csv_str.split("\\n")
#     dest_url = r'my_file.csv'
#     fx = open(dest_url, 'w')
#     for line in lines:
#         fx.write(line + "\n")
#     fx.close()
#
# download_my_url(my_url)

def first_func(x, y):
    sumxy = x + y
    #return sumxy #does not 'print' the output in Python 3
    print(sumxy)

first_func(3, 5)

