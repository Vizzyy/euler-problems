#
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

import datetime

start = datetime.datetime.now()
print(start)


def amicable_num_sum(base_num):
    amicable_nums = []
    for i in range(1, base_num//2):
        if base_num % i == 0:
            if i not in amicable_nums:
                amicable_nums.append(i)
            if base_num//i != base_num and base_num//i not in amicable_nums:
                amicable_nums.append(base_num//i)

    amicable_nums.sort()
    return sum(amicable_nums)


total_sum = 0
amicable_pairs = []
for i in range(4, 10000):
    a = amicable_num_sum(i)
    b = amicable_num_sum(a)

    if i == b and a != b:
        pair = [a, b]
        pair.sort()
        if pair not in amicable_pairs:
            amicable_pairs.append(pair)

print(amicable_pairs)

for pair in amicable_pairs:
    total_sum += sum(pair)

print(total_sum)
print(f"FINISHED")
end = datetime.datetime.now() - start
print(end)

#runtime 0:00:01.929461