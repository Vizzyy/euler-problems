#
#
# The primes 3, 7, 109, and 673, are quite remarkable.
# By taking any two primes and concatenating them in any order the result will always be prime.
# For example, taking 7 and 109, both 7109 and 1097 are prime.
# The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
import copy
import datetime
import sympy

start = datetime.datetime.now()
print(start)


non_primes = []
counter = 0


def all_concatenations_prime(prime_list, base_num):
    global counter
    counter += 1
    if counter % 1000000 == 0:
        print(f"Testing combinations {counter}... {datetime.datetime.now() - start} "
              f"- prime_list {prime_list} -- base_num: {base_num}")

    for number in prime_list:
        combined1 = int(str(number) + str(base_num))
        if not sympy.isprime(combined1):
            return False
        combined2 = int(str(base_num) + str(number))
        if not sympy.isprime(combined2):
            return False

    return True


primes = list(sympy.primerange(0, 10000))
primes.pop(primes.index(2))
primes.pop(primes.index(5))

print(f"Number of primes generated: {len(primes)} -- combinations: {len(primes) ** 5}")
print(primes[:10])


def find_remarkable_primes():
    global non_primes, counter
    primes_sum = 100000000000
    current_lowest_primes = []
    print(f"Testing combinations... {datetime.datetime.now() - start}")
    counter = 0
    for a in range(len(primes)):
        for b in range(a+1, len(primes)):
            candidate_primes = [primes[a]]
            if not all_concatenations_prime(candidate_primes, primes[b]):
                continue

            for c in range(b+1, len(primes)):
                candidate_primes = [primes[a], primes[b]]
                if not all_concatenations_prime(candidate_primes, primes[c]):
                    continue

                for d in range(c+1, len(primes)):
                    candidate_primes = [primes[a], primes[b], primes[c]]
                    if not all_concatenations_prime(candidate_primes, primes[d]):
                        continue

                    for e in range(d+1, len(primes)):
                        candidate_primes = [primes[a], primes[b], primes[c], primes[d]]
                        if not all_concatenations_prime(candidate_primes, primes[e]):
                            continue
                        else:
                            candidate_primes = [primes[a], primes[b], primes[c], primes[d], primes[e]]
                            sum_curr = sum(candidate_primes)
                            if sum_curr < primes_sum:
                                primes_sum = sum_curr
                                current_lowest_primes = copy.copy(candidate_primes)
                            print(f"Found {candidate_primes} after {datetime.datetime.now() - start} "
                                  f"with sum: {sum_curr}!")

    return current_lowest_primes


found = find_remarkable_primes()
print(sum(found))

print(f"FINISHED")
end = datetime.datetime.now() - start
print(end)

# 0:00:04.382202 for solution
# 0:00:58.645887 to confirm all combinations of primes under 10000