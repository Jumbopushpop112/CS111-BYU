from byu_pytest_utils import max_score, with_import

@max_score(5)
@with_import('lab24', 'count_occurrences')
def test_count_occurances(count_occurrences):
    s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    assert 3 == count_occurrences(s, 10, 9)

    s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    assert 2 == count_occurrences(s2, 3, 10)

    s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    assert 1 == count_occurrences(s, 1, 3)
    assert 3 == count_occurrences(s, 4, 2)

    s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    assert 2 == count_occurrences(s2, 6, 6)


@max_score(5)
@with_import('lab24', 'filter_gen')
@with_import('lab24', 'is_prime')
def test_filter_gen(is_prime, filter_gen):
    is_even = lambda x: x % 2 == 0
    assert [0, 2, 4] == list(filter_gen(range(5), is_even))

    all_odd = (2*y-1 for y in range(5))
    assert not list(filter_gen(all_odd, is_even))

    naturals = (n for n in range(1, 100))
    s = filter_gen(naturals, is_even)
    assert 2 == next(s)
    assert 4 == next(s)
    assert 6 == next(s)

    assert [2, 3, 5, 7] == list(filter_gen(range(1,8), is_prime))


@max_score(5)
@with_import('lab24', 'prime_numbers_gen')
def test_prime_numbers_gen(prime_numbers_gen):
    generated = prime_numbers_gen()
    assert 2 == next(generated)
    assert 3 == next(generated)
    assert 5 == next(generated)
    assert 7 == next(generated)
    assert 11 == next(generated)
    assert 13 == next(generated)
    assert 17 == next(generated)
    assert 19 == next(generated)
    assert 23 == next(generated)
    

@max_score(5)
@with_import('lab24', 'merge')
def test_merge(merge):
    def sequence(start, step):
        while True:
            yield start
            start += step
    a = sequence(2, 3)
    b = sequence(3, 2)
    result = merge(a, b)
    assert [2, 3, 5, 7, 8, 9, 11, 13, 14, 15] == [next(result) for _ in range(10)]


@max_score(0)
@with_import('lab24', 'repeated')
def test_repeated(repeated):
    s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    assert 9 == repeated(s, 2)

    s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    assert 8 == repeated(s2, 3)

    s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    assert 2 == repeated(s, 3)
    assert 5 == repeated(s, 3)

    s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    assert 2 == repeated(s2, 3)
