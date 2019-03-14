import re
import os
import glob
from collections import defaultdict
line = []
with open('largetable2.txt', 'wt') as f:
    for l in range(1,110):
        for c in range(1,110):
            line.append(str(l)+"."+str(c))
        for r in line:
            f.write(r + ";")
        f.write("\n")
        line.clear()
