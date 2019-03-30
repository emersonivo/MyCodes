import os
import re
#print(os.getcwd())


# HOMEDIR = os.path.dirname('/bkp_local/temp/')
# print("#1 ", HOMEDIR)
#
# TMPX = os.path.dirname(HOMEDIR+'/tmp/')
# bola = open(TMPX+'/test.txt','a')
# #texto = input("Type a message: ")
# bola.write("carro, rio, lua\n")
# bola.close()

# HOMEDIR = os.path.dirname('/bkp_local/temp/')
# print("#1 ", HOMEDIR)
# #
# # # Check if the folder '$HOMEDIR/data' exist in the current path, if not, create it
# datax = HOMEDIR+'/data'
# print("#2 ", datax)
# if not os.path.isdir(datax):
#     os.mkdir(datax,666)

import datetime
now = datetime.datetime.now()
timex = now.strftime('%Y%m%d%H%M%S')
print(timex)

MyDict = dict()
MyDict.update()