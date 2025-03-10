"""
Given an N x N MATRIX, find the maximum element in the matrix.

Input: [
            [3, 5, 9],
            [8, 1, 4],
            [7, 2, 6]
        ]
Output: 9
"""

def find_max(matrix):
    max_element = matrix[0][0]

    for row in matrix:
        for num in row:
            if num > max_element:
                max_element = num
    return max_element

matrix = [
    [3, 5, 9],
    [8, 1, 4],
    [7, 2, 6]
]

for row in matrix:
    print(row)
print()

print(find_max(matrix))