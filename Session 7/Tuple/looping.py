numbers = (10, 20, 30, 20, 40, 20, 50)

# for i in range(0, len(numbers)):
#     print(i, end=" ")

# print()


# i = 0
# while i < len(numbers):
#     print(i, end=" ")
#     i += 1

for index, value in enumerate(numbers):
    print(f"{index}. {value}")