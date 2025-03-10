"""
Given an N x N MATRIX, calculate the sum of diagonal elements.

Input: [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
Output: 15
"""

def diagonal_sum(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]
    return total

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7 ,8, 9]
]

for row in matrix:
    print(row)
print()

print(diagonal_sum(matrix))