'''
Separate a list of integers into two distinct lists: one
containing all the even numbers and the other
containing all the odd numbers.
'''

def even_odd(nums):
    even_nums = []
    odd_nums = []
    for i in nums:
        if i % 2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    return even_nums, odd_nums

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even, odd = even_odd(numbers)

print(f"Even Numbers: {even}\nOdd Numbers: {odd}")