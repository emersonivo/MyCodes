class Father():
    def surnamex(self):
        #print("Soares")
        return "Soares"
class Mother():
    def midlename(self):
        #print("Pereira")
        return "Pereira"
class Child(Father, Mother):
    pass
#    def namex(self):
#        print("Emerson")


newchild = Child()
#newchild.namex()
newchild.midlename()
newchild.surnamex()