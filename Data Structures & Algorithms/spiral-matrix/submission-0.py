class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom = 0, len(matrix)
        l, r = 0, len(matrix[0])

        while l < r and top < bottom:

            # get all i in top row
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1

            # get all i in right col
            for i in range(top, bottom):
                res.append(matrix[i][r-1])
            r -= 1

            if not(l<r and top<bottom):
                break

            # get all i in bottom row
            for i in range(r-1, l-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            # get all i in left col
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][l])
            l += 1
        
        return res
        