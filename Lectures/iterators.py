# Using the iter() function to create an iterator from an iterable object
nums = range(1, 4)
num_iter = iter(nums)
first = next(num_iter)

for num in num_iter:
    print(num)

# Is there a difference between using an iterator in a for loop and just using the iterable object itself?
# When might iterators be more useful?

# iterators maintain state (the position in the iterable object) across calls
nums = range(1, 4)
sum = 0
num_iter = iter(nums)
count = 0
for num in num_iter:
    print(num)
    count += 1
    if count > 1:
        break
# num_iter = iter(nums)
for num in num_iter:
    sum += num
print(sum)


# Functions that return iterators:
# reversed(): http://pythontutor.com/visualize.html#code=chocolate_bars%20%3D%20%28%2290%25%22,%20%2270%25%22,%20%2255%25%22%29%0A%0Aworst_first%20%3D%20reversed%28chocolate_bars%29%0A%0Afor%20chocolate%20in%20worst_first%3A%0A%20%20%20%20print%28chocolate%29&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
# zip(): http://pythontutor.com/composingprograms.html#code=eng_nums%20%3D%20%5B%22one%22,%20%22two%22,%20%22three%22%5D%0Aesp_nums%20%3D%20%5B%22uno%22,%20%22dos%22,%20%22tres%22%5D%0A%0Azip_iter%20%3D%20zip%28eng_nums,%20esp_nums%29%0Aeng,%20esp%20%3D%20next%28zip_iter%29%0Aprint%28eng,%20esp%29%0A%0Afor%20eng,%20esp%20in%20zip%28eng_nums,%20esp_nums%29%3A%0A%20%20%20%20print%28eng,%20esp%29&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D
# map(): http://pythontutor.com/visualize.html#code=nums%20%3D%20%5B1,%202,%203,%204,%205%5D%0A%0A%23%20Map%20returns%20an%20iterator%0Asquares1%20%3D%20map%28lambda%20num%3A%20num%20**%202,%20nums%29%0A%0A%23%20Create%20a%20list%20of%20all%20the%20elements%20from%20the%20iterator%0Asquares1%20%3D%20list%28squares1%29%0A%0A%23%20Compare%20to...%0Asquares2%20%3D%20%5Bnum**2%20for%20num%20in%20nums%5D&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
# filter(): http://pythontutor.com/visualize.html#code=nums%20%3D%20%5B1,%202,%203,%204,%205%5D%0A%0A%23%20Filter%20returns%20an%20iterator%0Aeven1%20%3D%20filter%28lambda%20num%3A%20num%20%25%202%20%3D%3D%200,%20nums%29%0A%0A%23%20Create%20a%20list%20of%20all%20the%20elements%20from%20the%20iterator%0Aeven1%20%3D%20list%28even1%29%0A%0A%23%20Compare%20to...%0Aeven2%20%3D%20%5Bnum%20for%20num%20in%20nums%20if%20num%20%25%202%20%3D%3D%200%5D&cumulative=true&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false


# Generator functions use yield instead of return. yield pauses the function and returns the specified value
# When the genrator function is called again, it picks up from where it had paused
# Python identifies a function as a generator if it contains a yield statement

# just call the generator function to get a generator object
def evens():
    num = 0
    while num < 10:
        yield num
        num += 2

evengen = evens()
print(next(evengen))
print(next(evengen))
print(next(evengen))
print(next(evengen))

# Looping over generators
def evens(start, end):
    num = start + (start % 2)
    while num < end:
        yield num
        num += 2

evengen = evens(12,20) 
for num in evengen:
   print(num)

# is this different in any way?
evens = [num for num in range(12, 20) if num % 2 == 0]
for num in evens:
    print(num)


# Exercise: write this generator function
def countdown(n):
    """
    Generate a countdown of numbers from n down to 'blast off!'.
    >>> c = countdown(3)
    >>> next(c)
    3
    >>> next(c)
    2
    >>> next(c)
    1
    >>> next(c)
    'blast off!'
    """
    while n > 0:
        yield n
        n -=1
    print("blast off")

c = countdown(3)
print(next(c))
print(next(c))
print(next(c))
print(next(c))

# Exercise: write this generator function to yield a sequence of Virahanka-Fibonacci numbers
def generate_virfib():
    """Generate the next Virahanka-Fibonacci number.
    >>> g = generate_virfib()
    >>> next(g)
    0
    >>> next(g)
    1
    >>> next(g)
    1
    >>> next(g)
    2
    >>> next(g)
    3
    """
    i = 0
    j = 1
    while True:
        yield i
        i,j = j, i+j

g = generate_virfib()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# the "yield from" statement can be used to yield the values from an iterable one at a time
def a_then_b(a, b):
    yield from a
    yield from b

f = a_then_b(["Apples", "Aardvarks"], ["Bananas", "BEARS"])

print(next(f))
print(next(f))
print(next(f))
print(next(f))

print(list(a_then_b(["Apples", "Aardvarks"], ["Bananas", "BEARS"])))


