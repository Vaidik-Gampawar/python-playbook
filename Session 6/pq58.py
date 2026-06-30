'''
Find the largest and smallest number
in a list without using built-in functions like
max() or min().
'''

def find_min_max(nums):
    mini = nums[0]
    maxi = nums[0]

    for i in nums:
        if i > maxi:
            maxi = i
        elif i < mini:
            mini = i
            
    return maxi, mini

nums =  [3, 1, 4, 1, 5]

maxi, mini = find_min_max(nums)
print(f"{maxi}, {mini}")

