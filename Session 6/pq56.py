'''
Given two lists of the same length, write Python code using a loop to create a new list where each element is the sum of the corresponding elements from both original lists.
'''

def sum_of_two_list(list1, list2):
    new_list = []
    n = len(list1)
    for i in range(0, n):
        total = list1[i] + list2[i]
        new_list.append(total)
    return new_list

list1 = [10, 20, 30, 40]
list2 = [1, 2, 3, 4]

print(sum_of_two_list(list1, list2))

