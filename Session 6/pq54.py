'''
Write a program that takes a list and a target number. Use a loop to determine if the target number exists in the list. Do not use the in operator.
'''

def does_target_exists(lst, target):
    for num in lst:
        if num == target:
            return True
    return False

my_list = [10, 20, 30, 40, 50]

ans = does_target_exists(my_list, 60)
print(ans)

