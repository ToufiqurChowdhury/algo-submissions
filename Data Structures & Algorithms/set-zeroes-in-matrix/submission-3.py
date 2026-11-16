class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        zeros = []

        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeros.append((r,c))
        
        for r, c in zeros:
            for i in range(rows):
                matrix[i][c] = 0
            for j in range(cols):
                matrix[r][j] = 0
        
