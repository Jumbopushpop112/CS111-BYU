import sys
def printEachArgument(listArguments):
    for argument in listArguments:
        print(argument)
def validateArguments(listArguments):
    if listArguments[1] == "-p" or listArguments[1] == "-i" or listArguments[1] == "-h" or listArguments[1] == "-w" or listArguments[1] == "-r":
        return True
    else:
        return False
def flags(listArguments):
        defaultString = "Hello World"
        #flag choices
        if listArguments[1] == "-p":
            listArguments = listArguments[2:]
            printEachArgument(listArguments)
        elif listArguments[1] == "-i":
            print("Hello World")
        elif listArguments[1] == "-w":
            if len(listArguments) <=3:
                print("No Content Provided")
            else:
                with open(listArguments[2], "w") as file:
                    listArguments = listArguments[3:]
                    for line in listArguments:
                        file.write(line + "\n")
        elif listArguments[1] == "-r":
            with open(listArguments[2], "r") as file:
                for line in file:
                        print(line.strip("\n"))
        else:
            print("Valid flags:")
            print("-p : prints out all the command line arguments after the -p")
            print(f'-i : prints "{defaultString}"')
            print("-h : prints out a help command")
def main():
     if validateArguments(sys.argv):
         flags(sys.argv)
     else:
         printEachArgument(sys.argv)
main()

