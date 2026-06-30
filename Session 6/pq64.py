'''
Given a list of numbers (which may contain duplicates), write a
Python script that takes an integer as input from the user and
removes all occurrences of that integer from the list.
'''

def remove_duplicate(nums):
    n = int(input("Enter Value: "))
    for i in nums:
        if n in nums:
            nums.remove(n)
    return nums

my_list = [10, 20, 10, 30, 20, 10, 40]
print(remove_duplicate(my_list))