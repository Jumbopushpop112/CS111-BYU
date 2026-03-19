def sum_digits(n):
    """Returns the sum of the digits of positive integer N.
    >>> sum_digits(6)
    6
    >>> sum_digits(2023)
    7
    """
    if n < 10:       # base case
        return n
    else:            # recursive case
        last = n % 10
        all_but_last = n // 10
        return sum_digits(all_but_last) + last

print(sum_digits(6))
print(sum_digits(2023))

def fact(n):
    """Returns the factorial of N.
    >>> fact(0)
    1
    >>> fact(3)
    6
    """
    if n == 0:              # base case
        return 1
    else:                   # recursive case
        return n*fact(n-1)

print(fact(7))

# now with print statments to help understanding
def fact(n):
    """Returns the factorial of N.
    >>> fact(0)
    1
    >>> fact(3)
    6
    """
    if n == 0:              # base case
        print('n=0')
        return 1
    else:                   # recursive case
        print(f'n={n} and n-1={n-1}')
        factorial = n*fact(n-1)
        print(f'value of n*n-1={factorial}')
        return factorial

print(fact(7))



def luhn_sum(n):
    """Returns the Luhn sum for the positive number N.
    >>> luhn_sum(32)
    8
    >>> luhn_sum(5105105105105100)
    20
    """
    if n < 10:
        return n
    else:
        last = n % 10
        all_but_last = n // 10
        return luhn_sum_double(all_but_last) + last
        
def luhn_sum_double(n):
    last = n % 10
    all_but_last = n // 10
    luhn_digit = last * 2
    if luhn_digit > 9:
        luhn_digit = sum_digits(luhn_digit)
    return luhn_sum(all_but_last) + luhn_digit

print(luhn_sum(7492))
print(luhn_sum(5105105105105100))



# For you to try to code recursively
def sum_nums(nums):
    """Returns the sum of the numbers in nums.
    >>> sum_nums([2,3,4])
    9
    >>> sum_nums([6, 24, 1984])
    2014
    >>> sum_nums([-32, 0, 32])
    0
    """
    pass

print(sum_nums([2,3,4]))

# For you to try to code recursively
def sum_up_to(n):
    """Returns the sum of positive numbers from 1 
    up to n (inclusive).
    >>> sum_up_to(5)
    15
    """
    pass

print(sum_up_to(5))
