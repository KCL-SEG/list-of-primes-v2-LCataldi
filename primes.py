"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError

    number_to_check = 0
    while len(list) != number_of_primes:

        is_prime = True
        if number_to_check <= 1:
            is_prime = False
        for i in range(2, int(number_to_check ** 0.5) + 1):
            if number_to_check % i == 0:
                is_prime = False

        if is_prime:
            list.append(number_to_check)

        number_to_check = number_to_check + 1

    return list