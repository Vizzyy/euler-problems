# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

with open('p13input.txt') as f:
    input_string = f.readlines()

# this is easy, just cast as float
sanitized = [float(line.strip()) for line in input_string]

sum = 0.0
for line in sanitized:
    sum += line

# and then manipulate the string ignoring the exponent, moving the decimal, and truncating digits
print("" + str(sum).split('.')[0] + str(sum).split('.')[1][:9])
