class Person:

    def __init__(self):
        self.name

    def getName(self):
        self.name += 'k'
        return self.name

    def setName(self, newName):
        self.name = newName

class Person2:

    def __init__(self):
        self.name

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

class Person3:

    def __init__(self):
        self.name
        self.lastname

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getLast(self):
        return self.last

    def setLast(self, newLast):
        self.last = newLast