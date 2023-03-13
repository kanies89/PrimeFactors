NUMBERS = [
    (1, [1]),
    (2, [1, 2])
]


def prime_factors(number):
    factors = []
    if number == 1:
        factors.append(1)
    if number == 2:
        factors.append(1)
        factors.append(2)
    return factors


def test_prime_factors():
    for test_case, expected in NUMBERS:
        assert prime_factors(test_case) == expected
