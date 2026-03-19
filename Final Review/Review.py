import sys
print(sys.argv)
message = input("Enter a message")
print(message)

with open("file.txt","w") as f:
    f.write("Hello world")

def func1(func):
    def func2(x):
        return func(x)
    return func2
print(func1(lambda x: x**2)(9))

class Link:
    empty = ()
    def __init__(self,value,next=empty):
        self.value = value
        self.next = next
l1 = Link(1)
l2 = Link(2,l1)
l3 = Link(3,l2)

while l3 is not Link.empty:
    print(l3.value)
    l3 = l3.next
