'''
Ask a number from the user, and print all the factors
'''

num = int(input("Enter a number: "))

original_num = num
i = 1
count = 0

# Factorial is not defined for negative numbers
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    while i <= num:
        if num % i == 0:
            print(i)
            count = count + 1
        i = i + 1

print(count)
