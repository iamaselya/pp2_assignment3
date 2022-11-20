class String:
    def __init__(self, string):
        self.string = string

    def getString(self):
        return self.string

    def printString(self):
        return self.string.upper()

s = String(input())
print(s.getString(), s.printString())