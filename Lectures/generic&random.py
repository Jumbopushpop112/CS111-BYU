# Generic function
def sum_em(items, initial_value):
    """Returns the sum of ITEMS,
    starting with a value of INITIAL_VALUE."""
    sum = initial_value
    for item in items:
        sum += item
    return sum

print(sum_em(range(4),0))
print(sum_em(["a", "b", "c"],""))
# Generic function end

# Type dispatching
def is_valid_month(month):
    if isinstance(month, str):
        if len(month) == 1:
            return month in ["J", "F", "M", "A", "S", "O", "N", "D"]
        else:
            return month in ["January", "February", "March", "April",
                "May", "June", "July", "August", "September",
                "October", "November", "December"]
    if isinstance(month, int):
        return month >= 1 and month <= 12
    return False

print(is_valid_month("N"))
print(is_valid_month("July"))
print(is_valid_month(13))
# Type dispatching end

# Type Coercion
from math import gcd
class Rational:
    def __init__(self, numerator, denominator):
        g = gcd(numerator, denominator)
        self.numer = numerator // g
        self.denom = denominator // g
    def __add__(self, other):
        new_numer = self.numer * other.denom + other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)
    def __str__(self):
        return f"{self.numer}/{self.denom}"
    def __repr__(self):
        return f"Rational({self.numer}, {self.denom})"

print(Rational(1,2))
print(Rational(1, 2) + Rational(3, 4))

def sum_numbers(nums):
    """Returns the sum of nums"""
    sum = Rational(0, 1)
    for num in nums:
        if isinstance(num, int):
            num = Rational(num, 1)
        sum += num
    return sum

print(sum_numbers([1,Rational(5,2),3]))
# Type Coercion end

#Random number demo
from random import randrange, seed, random
from math import sqrt
def calc_pi(n):
    count = 0
    for i in range(n):
        x = random()
        y = random()
        if sqrt(x * x + y * y) <= 1.0:
            count += 1
    print(f"With n={n:8}, pi = {4 * count / n}")

for s in [1,1,2,3]:
    seed(s)
    print(f"seed = {s}:", end=" ")
    for i in range(10):
        print(randrange(1, 100), end=" ")
    print()

print()
for i in range(1, 9):
    calc_pi(10 ** i)
#Random number demo end
