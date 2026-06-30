'''
Create a list containing the squares of numbers
from 1 to 10 (i.e., [1, 4, 9, ..., 100]).
'''

def square_list(nums):
    result = []
    for i in nums:
        result.append(i**2)
    return result

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(square_list(data))