NUMBERS = [
    (1, 1),
    (2, [1, 2])
]


def prime_factors(number):
    if number == 1:
        return 1


def test_prime_factors():
    for test_case, expected in NUMBERS:
        assert prime_factors(test_case) == expected
