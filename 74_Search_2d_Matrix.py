# Brute force solution
from typing import List


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    row = len(matrix)-1
    cols = len(matrix[0])-1

    for i in range(row):
        for j in range(cols):
            if target == matrix[i][j]:
                return True

    return False

# better solution
# O(n+m) time | O(1) space


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    row = 0  # first index of the matrix
    col = len(matrix[0])-1  # Last index of the matrix
    # traversing the matrix

    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1  # moving to the left
        elif matrix[row][col] < target:
            row += 1  # moving down
        else:
            return True
    return False
