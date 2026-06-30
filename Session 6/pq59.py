'''
Reverse a list without using the
.reverse() method or list slicing ([::-1]).
'''

def reverse_list(nums):
    n = len(nums)
    rev_list = []
    for i in range(n-1, -1, -1):
        rev_list.append(nums[i])
    return rev_list

lst = [1, 2, 3, 4, 5, 6]

print(reverse_list(lst))