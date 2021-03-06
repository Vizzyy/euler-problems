#
#
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
# 1: 1
# 3: 1,3
# 6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?
import datetime

start = datetime.datetime.now()
print(start)
triangle_sums = [0]


def triangle_sum(number):
    prev_sum = triangle_sums[number-1]
    new_sum = number + prev_sum
    triangle_sums.append(new_sum)
    return new_sum


# generate first 1 mil tri sums upfront
for i in range(1, 1000000):
    triangle_sum(i)


def get_factors(number):
    factors = []
    i = 1

    # we iterate from i < sqrt(number)
    while i*i <= number:
        if number % i == 0:
            factors.append(i)  # append factor

            # this bit is the magic
            if number//i != i:
                factors.append(number//i)
        i += 1

    return factors


for num in range(1, 15):
    print(get_factors(triangle_sum(num)))


number = 0
highest_factor_count = 0
increment = 1
while True:
    number += increment
    tri_sum = triangle_sums[number]

    factor_count = len(get_factors(tri_sum))
    if factor_count > highest_factor_count:
        highest_factor_count = factor_count
        print(f"number: {number} - tri_sum: {tri_sum} - highest_factor_count: {highest_factor_count}")

    if factor_count > 500:
        first_found = number
        break

end = datetime.datetime.now() - start
print(end)

# 0:00:05.337753 exec time