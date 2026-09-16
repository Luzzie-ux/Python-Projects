def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    for x in matrix:
        x.reverse()
    return matrix
