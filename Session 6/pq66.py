'''
Using list comprehension, create a list of squares of all odd numbers from 1 to 20.
'''

new_list = [i**2 for i in range(1, 20) if i%2 != 0]
print(new_list)