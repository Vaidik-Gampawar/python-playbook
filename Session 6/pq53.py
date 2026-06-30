'''
Given a list of numbers, write Python code using a loop to find and print the largest element. Do not use the built-in max() function.
'''

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

maxi = float("-inf")

for i in numbers:
    if i > maxi:
        maxi = i
print(maxi)