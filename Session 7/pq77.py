'''
 Take 5 numbers as input from the user, store them in a tuple, and print the tuple along with its minimum and maximum
'''


numbers_list = []

print("Please enter 5 numbers:")

for i in range(1, 6):
    num = eval(input(f"Enter number {i}: "))
    numbers_list.append(num)

number_tuple = tuple(numbers_list)

print(number_tuple)
print(max(number_tuple))
print(min(number_tuple))