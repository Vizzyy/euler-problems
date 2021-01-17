
#
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?



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