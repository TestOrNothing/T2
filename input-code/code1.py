
class Person:
    def __init__(self, firstName, lastName, a):
        self.firstName = firstName
        self.lastName = lastName
        self.a = a

    def fullName(self):
        return self.firstName + self.lastName

    def doit(self):
        eval("2+2")

    def somethig(self):
        if True:
            print("something")

    def notUse(self):
        x = 1  # NeverReadedVariable
        y = 2
        x += y
        return 1 + 1

class Person2:
    def __init__(self):
        self.name

    def getName(self):
        return self.name

    def setName(self,newName):
        self.name = newName


