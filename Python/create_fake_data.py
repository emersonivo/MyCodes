import os
import random

HOMEDIR = os.path.dirname('/bkp_local/temp/')
print("#1 ", HOMEDIR)
#
datax = HOMEDIR+'/data'
if not os.path.isdir(datax): # Check if the folder '$HOMEDIR/data' exist in the current path, if not, create it
    os.mkdir(datax,666)

tmpx = HOMEDIR+'/tmp'
if not os.path.isdir(tmpx): # Check if the folder '$HOMEDIR/tmp' exist in the current path, if not, create it
    os.mkdir(tmpx, 666)

name = ['Paul', 'John', 'Elizabeth', 'Joe', 'George', 'Mark', 'Mary', 'Jane']
loc = ['Canada', 'USA', 'Germany']
res2 = ['sysloc', 'windir', 'windfs', 'winperm']
status = ['INPROCESS', 'REQUESTED', 'PROVISIONED', 'FAILED']

with open(tmpx+"/file.txt", "w") as OUTPUT:
    for x in range(1,10):
        OUTPUT.write("Resource: "+"\n")
        OUTPUT.write("  Attribute: "+"\n")
        OUTPUT.write("    uid: " + str(random.uniform(111111, 999999)) + "\n")
        OUTPUT.write("    Name: "+random.choice(name)+"\n")
        OUTPUT.write("    Country: "+random.choice(loc)+"\n")
        OUTPUT.write("    Sysloc: "+"\n")
        OUTPUT.write("     Valor: " + random.choice(status)+"\n")
        OUTPUT.write("    Windir: "+"\n")
        OUTPUT.write("     Valor: " + random.choice(status)+"\n")
        OUTPUT.write("    Windfs: "+"\n")
        OUTPUT.write("     Valor: " + random.choice(status)+"\n")
        OUTPUT.write("    Winperm: "+"\n")
        OUTPUT.write("     Valor: " + random.choice(status)+"\n")
        OUTPUT.write("\n")