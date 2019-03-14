# #https://stackoverflow.com/questions/26659142/cat-grep-and-cut-translated-to-python
print("------------ Semicolon delimited ------------------")
with open("/mnt/usb-SanDisk_Ultra_4C531001510331103462-0:0-part1/PycharmProjects/untitled/Semicolon_delimited.txt") as file1:
    for line1 in file1:
        if not "House" in line1:
            continue
        try:
            print(line1)
            print("Semicolon delimited: ", line1.split(';')[1])
        except IndexError:
            print
# print("------------- Tab delimited -----------------")
# with open("/mnt/usb-SanDisk_Ultra_4C531001510331103462-0:0-part1/PycharmProjects/untitled/Tab_delimited.txt") as file2:
#     for line2 in file2:
#         if not "House" in line2:
#             continue
#         try:
#             print(line2)
#             print("Semicolon delimited: ", line2.split('\t')[:1])
#         except IndexError:
#             print
# print("--------------- Word delimited ---------------")
# with open("/mnt/usb-SanDisk_Ultra_4C531001510331103462-0:0-part1/PycharmProjects/untitled/Text_delimited.txt") as file3:
#     for line3 in file3:
#         if not "delimiter" in line3:
#             print(line3)
#             continue
#         try:
#             print("Full line", line3)
#             newline3 = line3.split('delimiter')[1]
#             print("First delimiter: ", newline3)
#             if not "fields" in newline3:
#                 continue
#             try:
#                 print("Full line", line3)
#                 print("Text_delimited: ", newline3.split('fields')[0])
#             except IndexError:
#                 print
#         except IndexError:
#             print