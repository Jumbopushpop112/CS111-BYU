def largest_factor(n):
    biggest_factor = 1
    i = 2
    if n == 1 or n == 0:
        return 1
    while i < n:
        if n % i == 0:
            biggest_factor = i
        i += 1

    return biggest_factor


def missing_digits(n):
    counter = 0
    while n > 10:
        last_digit = n % 10
        second_to_last_digit = (n // 10) % 10
        diff = last_digit - second_to_last_digit
        if diff == 0:
            return 0
        counter += diff-1
        n //= 10

    return counter
print(largest_factor(100))
print(missing_digits(39))