class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        zeros = []

        m = len(matrix)
        n = len(matrix[0])

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zeros.append((r,c))

        
        for r, c in zeros:
            for i in range(m):
                matrix[i][c] = 0
            for j in range(n):
                matrix[r][j] = 0
        
        
        