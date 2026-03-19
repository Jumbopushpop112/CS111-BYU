#high order function, which returns a function
def stringIt():
    def printIt(string):
        return string
    return printIt
x = stringIt()
print(x("Hello"))