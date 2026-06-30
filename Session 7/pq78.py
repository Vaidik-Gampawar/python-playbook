'''
Write a function get_stats(nums) that takes a tuple of numbers and returns a tuple containing the sum, average, minimum, and maximum. Unpack
the returned tuple and print each value.
'''

def get_stats(nums):
    total = sum(nums)
    avg = total / len(nums)
    mini = min(nums)
    maxi = max(nums)

    return (total, avg, mini, maxi)

total, avg, mini, maxi = get_stats((34, 23, 42, 412, 34, 43))

print(total)
print(avg)
print(mini)
print(maxi)