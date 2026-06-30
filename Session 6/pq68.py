'''
Create a 3x3 matrix (a nested list) and then use nested loops to calculate and print the sum of all its elements.
'''

matrix = [
    [4, 8, 1],
    [9, 7, 2],
    [5, 6, 0],
]

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
         print(f"{matrix[i][j]}", end=" ")
    print()