class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # row = m//COLS
        # col = m%Cols
        
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, (ROWS * COLS)-1

        while l<=r:
            m = l + (r-l) //2

            row, col = m//COLS, m%COLS

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m+1
            else:
                r = m-1

        return False 
        