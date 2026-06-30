matrix = [
    [4, 8, 1, 2, 1],
    [9, 7, 2, 6, 3],
    [5, 6, 0, 3, 5],
    [8, 4, 3, 9, 3],
]

rows = len(matrix)
columns = len(matrix[0])

for i in range(0, rows):
    for j in range(0, columns):
        print(f"{matrix[i][j]}", end=" ")
    print()