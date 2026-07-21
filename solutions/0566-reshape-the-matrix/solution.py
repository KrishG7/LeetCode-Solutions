class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        new_mat = [[0] * c for _ in range(r)]
        count = 0

        for i in range(m):
            for j in range(n):
                new_mat[count // c][count % c] = mat[i][j]
                count += 1

        return new_mat

