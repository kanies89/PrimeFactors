from functools import wraps

NUMBERS = [
    (1, [1]),
    (2, [1, 2]),
    (3, [1, 3]),
    (4, [1, 2, 2]),
    (5, [1, 5]),
    (6, [1, 2, 3]),
    (7, [1, 7]),
    (8, [1, 2, 2, 2]),
    (49, [1, 7, 7]),
    (2135, [1, 5, 7, 61]),
    (6789, [1, 3, 31, 73])
]

DATA = [
    (1.1, "Not an integer"),
    ("Prime", "Not an integer")
]

primes = []


def check_input(func):
    @wraps(func)
    def wrapper(number):
        if not isinstance(number, int):
            raise ValueError("Not an integer")
        return func(number)

    return wrapper


def calculate_primes(num_given):
    global primes
    for num in range(3, num_given + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                primes.append(num)
                primes = list(set(primes))


@check_input
def prime_factors(number):
    global primes

    factors = []
    if number >= 1:
        factors.append(1)
    while number > 1:
        if number % 2 == 0:
            factors.append(2)
            number /= 2
        if number % 2 != 0 and number != 1:
            calculate_primes(int(number))

            for p in primes:
                if number % p == 0:
                    factors.append(p)
                    number /= p

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
