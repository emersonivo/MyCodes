import re
import os
import glob
from collections import defaultdict

global lines
global tmp
global homedir
global lastcel
global board
global lincol

Dlines = defaultdict(list)
mybkp = defaultdict(list)
Alines = []

for k in range(1, 5):
    for l in range(1, 5):
        for c in range(0, 9):
            cel = int(str(l)+str(c))
            Dlines[k].append(cel)
    print("Loop: ", k, Dlines[k])
print(len(Dlines))

r = 0
frst = ""
for key, value in Dlines.items():
    if 22 in value:
        line = Dlines[key]
        frst = line[0]
        print("Antes: ", frst, line)
        line.remove(22)
        print("Depois: ", frst, line)

        # for r in line:
        #     print(r)



        # print("Key: ", key, " Old: ", len(line), " ", line)
        # for x in range(22, 26):
        #     line.remove(x)
        # print("Key: ", key, " New: ", len(line), " ", line)

