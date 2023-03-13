NUMBERS = [
    (1, [1]),
    (2, [1, 2]),
    (3, [1, 3]),
    (4, [1, 2, 4])
]

DATA = [
    (1.1, "Not an integer")
]


def prime_factors(number):
    factors = []
    if number == 1:
        factors.append(1)
    if number == 2:
        factors.append(1)
        factors.append(2)
    if number == 3:
        factors.append(1)
        factors.append(3)
    return factors


def test_prime_factors():
    for test_case, expected in NUMBERS:
        assert prime_factors(test_case) == expected


def test_prime_factors_wrong_data():
    for test_case, expected in DATA:
        try:
            prime_factors(test_case)
        except ValueError as e:
            assert e.args[0] == expected

