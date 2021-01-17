#
#
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#     13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
import datetime

start = datetime.datetime.now()
print(start)

num_with_longest_chain = 1
longest_chain_length = 0
solved_numbers = {}

for i in range(1, 1000000):
    start_num = i
    current_num = start_num
    current_chain = 1

    while True:

        if current_num in solved_numbers.keys() and start_num != 1:
            current_chain += solved_numbers[current_num]
            current_num = 1
        else:
            if current_num % 2 == 0:
                current_num //= 2
            else:
                current_num = (3*current_num) + 1

            current_chain += 1

        if current_num == 1:
            if start_num not in solved_numbers.keys() and start_num != 1:
                solved_numbers[start_num] = current_chain

            if current_chain > longest_chain_length:
                print(f"i: {i} - {datetime.datetime.now() - start} - longest_chain_length: {longest_chain_length}")
                longest_chain_length = current_chain
                num_with_longest_chain = start_num
            break


print(f"FINISHED")
end = datetime.datetime.now() - start
print(end)
print(f"longest_chain_length: {longest_chain_length} - num_with_longest_chain: {num_with_longest_chain}")

# Memoization significantly improves performance:
# FINISHED
# 0:00:02.588012