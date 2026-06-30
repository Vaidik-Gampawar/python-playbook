'''
Given a 3x3 matrix, print only the anti-diagonal (top-right to bottom-left)
elements and replace everything else with an asterisk (*).
'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(0, 3):
    for j in range(0, 3):
        if i+j == len(matrix)-1:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()