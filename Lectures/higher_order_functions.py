# first-order function 
def cube(k):
    return k ** 3

# higher-order function
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

print(summation(5,cube))


# locally defined function - adder
def make_adder(n):
    """Return a function that takes one argument k
       and returns k + n.
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

add_three = make_adder(3)
print(add_three(4))
print(make_adder(3)(4))


# function composition
def happy(text):
    return "☻" + text + "☻"

def sad(text):
    return "☹" + text + "☹"

def composer(f, g):
    def composed(x):
        return f(g(x))
    return composed

print(sad(happy("CS 111!")))
print(composer(sad, happy)("CS 111!"))

composed = composer(sad, happy)
print(composed("CS 111!"))

msg1 = composer(sad, happy)("CS 111!")
print(msg1)

# function composition 2
def happy(text):
    return "☻" + text + "☻"

def make_texter(emoji):
    def texter(text):
        return emoji + text + emoji
    return texter

def composer(f, g):
    def composed(x):
        return f(g(x))
    return composed

print(composer(happy, make_texter("☃︎"))('snow day!'))
