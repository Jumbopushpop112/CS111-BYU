def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)
def multiply(m, n):
    """ Takes two positive integers (including zero) and returns
    their product using recursion.
    >>> multiply(5, 3)
    15
    """
    """*** YOUR CODE HERE ***"""
    if n == 1:
        return m
    elif n == 0:
        return 0
    return m + multiply(m,n-1)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    """*** YOUR CODE HERE ***"""
    # for num in range(2, n):
    #     if n % num == 0:
    #         return False
    # return True
    def is_prime_helper(n,current_divider):
        if current_divider == 1:
            return True
        elif n % current_divider == 0:
            return False
        else:
            return is_prime_helper(n,current_divider-1)
    return is_prime_helper(n,n-1)
