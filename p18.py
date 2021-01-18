#
#
# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
# it cannot be solved by brute force, and requires a clever method! ;o)
import copy
import datetime

start = datetime.datetime.now()
print(start)

with open('p18input.txt') as file:
    input_data = file.readlines()

pyramid = [[int(num) for num in line.strip().split(' ')] for line in input_data]
[print(line) for line in pyramid]

current_index = 0  # first element
current_row_index = 0  # top of pyramid
path_taken = [pyramid[current_row_index][current_index]]
highest_sum = 0
highest_sum_path = []


def calculate_path(path_taken, curr_row, current_index, next_row_index):
    global highest_sum_path, highest_sum
    curr_number = pyramid[curr_row][current_index]
    temp_path = copy.copy(path_taken)
    temp_path.append(curr_number)

    if next_row_index >= len(pyramid):
        if sum(temp_path) > highest_sum:
            highest_sum = sum(temp_path)
            highest_sum_path = temp_path
        return

    calculate_path(temp_path, curr_row + 1, current_index, next_row_index + 1)
    calculate_path(temp_path, curr_row + 1, current_index + 1, next_row_index + 1)


calculate_path([], current_row_index, current_index, current_row_index + 1)

print(f"highest_sum: {highest_sum} - highest_sum_path: {highest_sum_path}")

print(f"FINISHED")
end = datetime.datetime.now() - start
print(end)

# naive bruteforce
# runtime 0:00:00.024549