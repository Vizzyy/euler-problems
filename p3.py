#
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import math


def is_prime(number):
    print(f"checking: {number}")
    if number == 1:
        return False
    elif number <= 3:
        return True
    else:
        for i in range(2, math.ceil(number/2)):
            if number % i == 0:
                return False
        return True


highest_prime = None

for i in range(2, math.ceil(600851475143/2)):
    if 600851475143 % i == 0:
        if is_prime(i):
            highest_prime = i

print(f"highest: {highest_prime}")
