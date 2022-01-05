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
