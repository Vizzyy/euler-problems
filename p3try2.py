#
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import math


def is_prime(p):
    # http://rosettacode.org/wiki/AKS_test_for_primes
    if p == 2:
        return True
    c = 1
    for i in range(p // 2 + 1):
        c = c * (p - i) // (i + 1)
        if c % p:
            return False
    return True


highest_prime = None

for i in range(2, math.ceil(600851475143 / 2)):
    if 600851475143 % i == 0:
        if is_prime(i):
            highest_prime = i
            print(f"prime: {i}")

print(f"highest: {highest_prime}")
