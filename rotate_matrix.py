"""
Given an N x N MATRIX, rotate it 90 degrees clockwise.

Input: [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
Output: [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
"""

def rotate_matrix(matrix):
    transposed = []

    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        transposed.append(new_row)

    rotated = [row[::-1] for row in transposed]
    return rotated
    
matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

for row in matrix:
    print(row)
print()
rotated = rotate_matrix(matrix)
for row in rotated:
    print(row)