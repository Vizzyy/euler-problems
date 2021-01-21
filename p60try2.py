#
#
# The primes 3, 7, 109, and 673, are quite remarkable.
# By taking any two primes and concatenating them in any order the result will always be prime.
# For example, taking 7 and 109, both 7109 and 1097 are prime.
# The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.


import datetime
import json
import random
from itertools import combinations
import os.path

start = datetime.datetime.now()
print(start)


def is_prime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n != int(n):
        return False
    n = int(n)
    # Miller-Rabin test for prime
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(8):  # number of trials
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True


non_primes = []


def all_concatenations_prime(prime_list):
    global non_primes
    candidates = []
    for number in prime_list:
        for second_number in prime_list:
            if number == second_number:
                continue
            combined = str(number) + str(second_number)
            if combined not in non_primes:
                candidates.append(combined)
            else:
                return False
    # print(candidates)
    for candidate in candidates:
        if not is_prime(int(candidate)):
            non_primes.append(candidate)
            # print(f"{candidate} is not prime!")
            return False

    return True


primes = []
prime_upper_bound = 10000000

if not os.path.exists(f'./primes_under_{prime_upper_bound}.txt'):
    print(f"Populating primes under {prime_upper_bound}...")
    for i in range(prime_upper_bound):
        if is_prime(i):
            primes.append(i)
    with open(f'./primes_under_{prime_upper_bound}.txt', 'w+') as file:
        file.write(json.dumps(primes))
else:
    print(f"Loading primes under {prime_upper_bound}...")
    with open(f'./primes_under_{prime_upper_bound}.txt') as file:
        primes = json.loads(file.read())

first_x_primes = 1000
primes_subset = primes[:first_x_primes]
primes_subset.pop(primes_subset.index(2))  # can exclude 2 & 5 b/c they will always concat to non-prime
primes_subset.pop(primes_subset.index(5))
print(primes_subset[:10])


def find_remarkable_primes():
    global non_primes
    print(f"Testing combinations... {datetime.datetime.now() - start}")
    counter = 0
    for a in primes_subset:
        print(f"Testing combinations a {primes_subset.index(a)}... {datetime.datetime.now() - start}")
        for b in primes_subset:
            if a == b or not all_concatenations_prime([a, b]):
                continue
            for c in primes_subset:
                if c == a or c == b or not all_concatenations_prime([a, b, c]):
                    continue
                for d in primes_subset:
                    if d == c or d == a or d == b or not all_concatenations_prime([a, b, c, d]):
                        continue
                    for e in primes_subset:
                        if e == c or e == a or e == b or d == e:
                            continue
                        if all_concatenations_prime([a, b, c, d, e]):
                            print(f"Found after {counter} iterations!")
                            return [a, b, c, d, e]
                        # elif counter % 1000000 == 0:
                        #     print(f"Testing combinations {counter}... {datetime.datetime.now() - start}")
                        counter += 1

    return "Not found."


print(find_remarkable_primes())

print(f"FINISHED")
end = datetime.datetime.now() - start
print(end)

