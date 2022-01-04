def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    rows = len(mat)
    columns = len(mat[0])

    if rows*columns != r*c:
        return mat
    output = [[0 for i in range(c)] for j in range(r)]
    temp = []

    for i in range(rows):
        for j in range(columns):
            temp.append(mat[i][j])

        k = 0
    for i in range(r):
        for j in range(c):
            output[i][j] = temp[k]
            k += 1
    return output
