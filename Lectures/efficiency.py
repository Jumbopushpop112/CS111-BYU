# Eficiency
counter = [0]

def exp(b, n):
  counter[0] += 1
  if n == 0:
    return 1
  else:
    return b * exp(b, n-1)

print(exp(2,16), counter[0])

# This is a more efficient version!
counter = [0]

square = lambda x: x * x
def exp_fast(b, n):
    counter[0] += 1
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n//2))
    else:
        return b * exp_fast(b, n-1)

print(exp_fast(2,1024), counter[0])

# Recursive Virahanka-Fibonacci
counter = [0]

def virfib(n):
    counter[0] += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return virfib(n-2) + virfib(n-1)
    
print(virfib(7),counter[0])
