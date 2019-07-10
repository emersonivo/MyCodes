# import re
# with open("Text1", "r") as sources:
#     lines = sources.readlines()
# with open("Text1", "w") as sources:
#     for line in lines:
#         sources.write(re.sub(r';$', '', line))
# sources.close()

import re
import os
with open("newfile.txt", "r") as sources:
    lines = sources.readlines()
with open("newfile.txt", "w") as destx:
    #print(lines)
    for line in lines:
        #upx = (re.sub(r'$', ';', line))
        #print(upx)
        if "print \"" in line:
            line = re.sub(r'print \"', 'print(\"', line)
            line = re.sub('\n', '', line)
            line = re.sub(r'$', ')', line)
            #destx.write(line+'\n')
            #destx.write(re.sub(r'print \"', 'print(\"', line))
        else:
            line = re.sub('\n', '', line)
            #destx.write(line)
        destx.write(line+'\n')
destx.close()
sources.close()




# local = os.getcwd()
# print(local)