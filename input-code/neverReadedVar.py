class Person:
    def __init__(self, firstName, lastName, a):
        self.firstName = firstName
        self.lastName = lastName
        self.aa = a

    def fullName(self):
        return self.firstName + self.lastName

    def usingOne(self):
        xx = 2
        aa = 3
        return xx + 1

    def notUse(self):
        xx = 1  # NeverReadedVariable
        yy = 2
        return 3