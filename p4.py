#
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(input):
    string_input = str(input)
    start_ptr = 0
    end_ptr = len(string_input) - 1

    while start_ptr <= end_ptr:
        if string_input[start_ptr] is not string_input[end_ptr]:
            return False
        else:
            start_ptr += 1
            end_ptr -= 1

    return True


largest = 0

for x in range(1, 999):
    for y in range(1, 999):
        mult = x * y
        if is_palindrome(mult):
            if mult > largest:
                largest = mult

print(largest)
