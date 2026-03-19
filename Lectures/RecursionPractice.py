#factorial with recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
#fibonacci sequence with factorial
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
print(fib(6))
#sum digits from n to 1
def sumDigits(n):
    if n == 0:
        return 0
    else:
        return n + sumDigits(n-1)
#sum digits from 1 to n
def sumUpTo(n):
    if n == 1:
        return 1
    else:
        return n + sumUpTo(n-1)
print(sumDigits(4))
print(sumUpTo(4))
#sum digits with a list
def sumNums(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sumNums(nums[1:])
print(sumNums([1,2,3,4]))