# x = 1
# while True:
#     try:
#         number = int(input("Enter a integer number: "))
#         print(17/number)
#         break
#     except ValueError:
#         print("Only numbers are accepted")
#     except ZeroDivisionError:
#         print("Only numbers diff from zero are accepted")
#     finally:
#         print("Loop: ", x)
#         x+=1

# values = [1, 2, 3]
# #x = 2
# x = 5
# try:
#     y = values[x]
# except:
#     print("Exception")
# else:
#     print("Normal ", y)

values = [1, -2, 3]
try:
    for x in values:
        if x < 0:
            raise IndexError("Try again")
        print(x)
except IndexError as bola:
    #print("Exception")
    print(bola)
else:
    print("All done", y)