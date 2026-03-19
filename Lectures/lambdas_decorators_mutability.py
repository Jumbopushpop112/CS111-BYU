# using a lambda function instead of a def'd function
def summation(n, term):
    """Sum the first N terms of a sequence. TERM is a function
       that takes a single argument and returns a result.
    >>> summation(5, cube)
    225
    """
    total = 0
    k = 1
    while k <= n:
        total = total + term(k)
        k = k + 1
    return total

print(summation(5,lambda k: k ** 3))

# Lambda function with a conditional expression
result1 = lambda x: "x is greater than 10" if x > 10 else "x is less than or equal to 10"
print(result1(12))  # Output: x is greater than 10
print(result1(8))   # Output: x is less than or equal to 10

# Lambda function with nested conditional expressions
result2 = lambda x: "x is greater than 10" if x > 10 else ("x is less than 10" if x < 10 else "x is equal to 10")
print(result2(12))  # Output: x is greater than 10
print(result2(8))   # Output: x is less than 10
print(result2(10))  # Output: x is equal to 10

# Now you do it!
result = lambda x: "Stop!" if x == "red" else "Go!" if x == "green" else "Proceed with caution!"
print(result("red"))    # Output: Stop!
print(result("green"))  # Output: Go!
print(result("yellow")) # Output: Proceed with caution!


# tracing function
def trace1(f):
    """Return a function that takes a single argument, x, prints it,
    computes and prints F(x), and returns the computed value.
    >>> square = lambda x: x * x
    >>> trace1(square)(3)
    -> 3
    <- 9
    9
    """
    def traced(x):
        print("->", x)
        r = f(x)
        print("<-", r)
        return r
    return traced

# now as a "decorator" that always traces the function
@trace1
def square(x):
    return x * x
print(square(3))

# equivalent to:
def square(x):
    return x * x
square = trace1(square)
print(square(3))

# also equivalent to:
def square(x):
    return x * x
print(trace1(square)(3))


# list mutability

# append() adds a single element to a list
s = [2, 3]
t = [5, 6]
s.append(4)
print(s)
s.append(t)
print(s)

# extend() adds all the elements in one list to another list
s = [2, 3]
t = [5, 6]
s.extend(t)
print(s)
#s.extend(4) 

# pop() removes and returns the last element
s = [2, 3]
t = [5, 6]
t = s.pop()
print(s)
print(t)

# remove() removes the first element equal to the argument
s = [6, 2, 4, 8, 4]
s.remove(4)
print(s)

L = [1, 2, 3, 4, 5]
LL = L
print(L is LL)

L[2] = 6               # Replacing one element
print(L)

L[1:3] = [9, 8]        # Replacing multiple elements
print(L)

L[2:4] = []            # Deleting elements
print(L)

L[1:1] = [2, 3, 4, 5]  # Inserting elements
print(L)

L[len(L):] = [10, 11]  # Appending
print(L)

L = L + [20, 30]       # What's the difference here?
print(L)
print(LL)

L[0:0] = range(-3, 0)  # Prepending
print(L)


# mutation in function calls

# A function can change the value of any object in its scope.
def do_stuff_to(x):
    x[0] = 99

four = [1, 2, 3, 4]
print(four[0])
do_stuff_to(four)
print(four[0])

# Even without arguments:
def do_other_stuff():
    four[3] = 99        # four is in the parent (global) frame!

four = [1, 2, 3, 4]
print(four[3])
do_other_stuff()
print(four[3])

 # a tuple is immutable!
four = (1, 2, 3, 4)
print(four[0])
# do_stuff_to(four)
print(four[0])


# mutable default arguments are part of the function object
# each time the function is called, s is bound to the same list in this case
def f(s=[]):
    s.append('x')
    return len(s)

print(f())
print(f())
print(f())

