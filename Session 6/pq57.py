'''
Write a program that takes a list of numbers and, using a loop, determines whether it is sorted in ascending order. Print True if it is sorted, and False otherwise.
Do not use built-in sort or sorted() functions for checking.
'''

def check_order(lst):
    n = len(lst)
    for i in range(0, n-1):
        if lst[i] > lst[i+1]:
            return False
    return True

# numbers = [1, 5, 10, 15, 20]
numbers = [1, 10, 5, 15, 20]

print(check_order(numbers))