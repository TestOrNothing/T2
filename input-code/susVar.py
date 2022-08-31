class Person:
    def __init__(self, firstName, lastName, a):
        self.firstName = firstName
        self.lastName = lastName
        self.a = a

    def fullName(self):
        return self.firstName + self.lastName

    def notUse(self):
        x = 1  # NeverReadedVariable
        y = 2
        return x + y