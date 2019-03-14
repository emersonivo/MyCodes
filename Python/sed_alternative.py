# import re
# with open("Text1", "r") as sources:
#     lines = sources.readlines()
# with open("Text1", "w") as sources:
#     for line in lines:
#         sources.write(re.sub(r';$', '', line))
# sources.close()

import re
import os
with open("Text1", "r") as sources:
    lines = sources.readlines()
with open("output.txt", "w") as destx:
    #print(lines)
    for line in lines:
        #upx = (re.sub(r'$', ';', line))
        #print(upx)
        destx.write(re.sub(r'$', ';', line))
destx.close()
sources.close()




# local = os.getcwd()
# print(local)