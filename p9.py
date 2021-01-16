#
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#     a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import sys

numbers = [num for num in range(1, 1001)]
# print(numbers)

add_up_to_thousand = []

for x in numbers:
    for y in numbers:
        if y == x or y < x:
            continue
        for z in numbers:
            if z == y or z == x or z < y:
                continue
            if x + y + z == 1000:
                if x**2 + y**2 == z**2:
                    print([x,y,z])
                    print(x * y * z)
                    sys.exit()

# print(add_up_to_thousand)