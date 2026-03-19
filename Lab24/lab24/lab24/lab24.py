def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n/2)+1):
        if (n % i) == 0:
            return False

    return True
def count_occurrences(t, n, x):
    """Return the number of times that x appears in the first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s2, 3, 10)
    2
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(s, 1, 3)
    1
    >>> count_occurrences(s, 4, 2)
    3
    >>> next(s)
    2
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> count_occurrences(s2, 6, 6)
    2
    """
    """*** YOUR CODE HERE ***"""
    countX = 0
    counter = 0
    for item in t:
        if item == x:
            countX += 1
        counter += 1
        if counter == n:
            break
    return countX


def filter_gen(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_gen(range(5), is_even)) # a list of the values yielded from the call to filter_gen
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_gen(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_gen(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    """*** YOUR CODE HERE ***"""
    for item in iterable:
        if fn(item):
            yield item

def prime_numbers_gen():
    """
    >>> gen = prime_numbers_gen()
    >>> next(gen)
    2
    >>> next(gen)
    3
    >>> next(gen)
    5
    >>> next(gen)
    7
    >>> next(gen)
    11
    """
    """*** YOUR CODE HERE ***"""
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1




def merge(a, b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    """*** YOUR CODE HERE ***"""
    c = next(a)
    d = next(b)
    while True:
        if c > d:
            yield d
            d = next(b)
        elif c < d:
            yield c
            c = next(a)
        else:
            yield c
            c = next(a)
            d = next(b)



# OPTIONAL
def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row.
    Iterate through the items such that if the same iterator is passed into
    the function twice, it continues in the second call at the point it left
    off in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    """*** YOUR CODE HERE ***"""


def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n/2)+1):
        if (n % i) == 0:
            return False

    return True
