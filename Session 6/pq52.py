'''
Create a list of numbers (e.g., [5, 2, 8, 1, 9, 3]). Print the list in ascending order and then in descending order using the sorted() function.
After printing, verify and print the original list to confirm it remains unchanged.
'''

data = [5, 2, 8, 1, 9, 3]


def sort_data(data):
    ascending = sorted(data)
    descending = sorted(data, reverse=True)

    return ascending, descending

ascending, descending = sort_data(data)
print(ascending)
print(descending)
print(data)
