'''
Create a list of 5 of your favourite movies. Print the first, last, and middle movie from your list using both positive and negative indexing where appropriate.
'''

marks = [23, 33, 53, 32, 11, 34, 76, 46, 97, 45, 5, 43, 45]

n = len(marks)
print(f"First element: {marks[0]}")
print(f"Last element: {marks[-1]}")
print(f"Middle Element: {marks[n//2 - 1]}")