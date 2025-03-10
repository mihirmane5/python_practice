"""
Given an N x N MATRIX, print the elements in flipped manner.

Input: [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
Output: [
            [3, 2, 1],
            [6, 5, 4],
            [9, 8, 7]
        ]
"""

def flip_horizontal(matrix):
    return [row[::-1] for row in matrix]
    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    print(row)
print()

flipped = flip_horizontal(matrix)
for row in flipped:
    print(row)