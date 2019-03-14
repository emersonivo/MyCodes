#num = int(input("Enter a number: "))
num = 19
if num < 18:
    print("You are too young")
elif num > 18 and num < 21:
    print("You are almost there")
else:
    print("You are good, go ahead and have a sit")

name = str(input("Enter your name: "))
#name = "Emerson"
if name == "Emerson" :
    print("You are me")
elif name == "Debora" :
    print("Your are my wife")
elif name == "Justin" :
    print("You are my son")
elif name == "Giovana" :
    print("You are my daughter")
else:
    print("I don't know you")