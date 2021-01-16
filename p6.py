# The sum of the squares of the first ten natural numbers is,
#
# The square of the sum of the first ten natural numbers is,
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
#
# .
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_squares = 0
square_sum = 0
nums = [num for num in range(1, 101)]
print(nums[99])

for num in nums:
    square_sum += num

square_sum = square_sum ** 2

for num in nums:
    sum_squares += num ** 2

print(f"sum_squares: {sum_squares}")
print(f"square_sum: {square_sum}")
print(square_sum - sum_squares)
