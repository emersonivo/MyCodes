# class War:
#     life = 5
#     def attack(self):
#         self.life -= 1
#
#     def defeat(self):
#         self.life += 1
#
#     def checkLifes(self):
#         if self.life <= 0:
#             print("I am dead", self.life)
#             exit()
#         elif self.life > 0 and self.life < 2:
#             print("You have to defeat: ", self.life)
#         else:
#             print("Keep going: ", self.life)
#
# battle1 = War()
# while True:
#     try:
#         action = int(input("Defeat [1] or Attack [0]: "))
#         if action is int:
#             if action == 1:
#                 battle1.defeat()
#                 battle1.checkLifes()
#             elif action == 0:
#                 battle1.attack()
#                 battle1.checkLifes()
#             else:
#                 print("Wrong choice. Try again.")
#     except ValueError:
#         print("Only numbers are accepted")
#     finally:
#         battle1.checkLifes()

class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -=amount

    def get_balance(self):
        return self.balance

a1 = Account(0)
a2 = Account(300)

a1.deposit(100)
a1.withdraw(40)
a2.deposit(400)
print("Balance is ", a1.get_balance())
print("Balance is ", a2.get_balance())