def cascade(n):
    """ prints shrinking and then growing numbers of digits of N """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

cascade(123)


def inverse_cascade(n):
    """ prints growing and then shrinking numbers of digits of N """
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

inverse_cascade(1234)


def virfib(n):
    """Compute the nth Virahanka-Fibonacci number, for N >= 1.
    >>> virfib(2)
    1
    >>> virfib(6)
    8
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return virfib(n-2) + virfib(n-1)
    
print(virfib(5))


def count_partitions(n, m):
    """
    Count the number of partitions of a positive integer N, using parts up to size M
    >>> count_partitions(6, 4)
    9
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m

n = 3
m = 2
print(f"Number of partitions: {count_partitions(n,m)}")
