#
#
# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
#
# NOTE: Do not count spaces or hyphens.
# For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.


import datetime

from num2words import num2words

start = datetime.datetime.now()
print(start)
#
# number = 42
# number_split = [int(num) for num in str(number)]
#
# ones_place = {
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine",
# }
#
# tens_place = {
#     1: "ten",
#     2: "twenty",
#     3: "thirty",
#     4: "forty",
#     5: "fifty",
#     6: "sixty",
#     7: "seventy",
#     8: "eighty",
#     9: "ninety",
# }
#
# teens = {
#     1: "eleven",
#     2: "twelve",
#     3: "thirteen",
#     4: "fourteen",
#     5: "fifteen",
#     6: "sixteen",
#     7: "seventeen",
#     8: "eighteen",
#     9: "nineteen",
# }
#
# spelled_out = ""
# digit_count = len(number_split)
# for i in range(digit_count, -1, -1):
#     digit = number_split[i]
#
#     # right-most digit
#     if i == digit_count - 1:
#         if digit == 0:
#             continue
#         else:
#             spelled_out += ""
#
#

# shelling out this worthless library is a waste of time

# python3 -m pip install num2words

letter_count = 0
for i in range(1, 1001):
    number_words = num2words(i)
    print(number_words)
    number_words = number_words.replace('-', '').replace(' ', '')
    print(number_words)
    print(len(number_words))
    letter_count += len(number_words)

print(letter_count)

# or in one line
print(sum([len(num2words(i).replace('-', '').replace(' ', '')) for i in range(1, 1001)]))



print(f"FINISHED")
end = datetime.datetime.now() - start
print(end)

