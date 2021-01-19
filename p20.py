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


def factorial(number):
    result = number
    for i in range(1, int(number)):
        result *= (number - i)

    return result


factorial_result = factorial(100)

factorial_digits = [int(digit) for digit in str(factorial_result)]
print(factorial_result)
print(factorial_digits)

print(f"sum of digits: {sum(factorial_digits)}")

print(f"FINISHED")
end = datetime.datetime.now() - start
print(end)
