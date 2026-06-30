#      0   1   2   3   4   5   6   7   8   9   10
lst = [12, 23, 54, 32, 42, 67, 21, 86, 76, 45, 77]

# total = 0
# for i in range(0, len(lst)):
#     total = total + lst[i]
# print(total)

# total = 0
# for i in lst:
#     total = total + i
# print(total)

total = 0
for i in lst[::-1]:
    total = total + i
print(total)