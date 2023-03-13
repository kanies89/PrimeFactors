NUMBERS = [
    (1, [1]),
    (2, [1, 2]),
    (3, [1, 3]),
    (4, [1, 2, 2]),
    (5, [1, 5])
]

DATA = [
    (1.1, "Not an integer")
]


def prime_factors(number):
    if not isinstance(number, int):
        return "Not an integer"
    factors = []
    primes = []
    if number >= 1:
        factors.append(1)
    while number > 1:
        if number % 2 == 0:
            factors.append(2)
            number = number / 2
        if number == 3:
            factors.append(3)
            number = number / 3
        if number % 2 != 0 and number % 3 != 0 and number != 1:
            primes.append(number)
            factors.append(number)
            number = number / number
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

