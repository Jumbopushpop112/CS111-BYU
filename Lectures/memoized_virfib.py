counter = [0]

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized


@memo
def virfib(n):
    counter[0] += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return virfib(n-2) + virfib(n-1)
    

print(virfib(20))
print(f"Called virfib {counter[0]} times.")