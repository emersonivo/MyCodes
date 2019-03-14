import re
import os
import glob

i = 10
Exit = 0
while Exit == 0:
    if i == 3:
        print("Saindo")
        exit
    else:
        i -= 1
        print(i)
