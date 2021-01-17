#
#
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?


import datetime

start = datetime.datetime.now()
print(start)

start_num = 0
exponent = 1000

for i in range(exponent):
    start_num = start_num | (1 << i)
start_num += 1

final = 0
for char in [char for char in str(start_num)]:
    final += int(char)

print(final)

print(f"FINISHED")
end = datetime.datetime.now() - start
print(end)

# runtime 0:00:00.000370