class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):
            nonlocal numPaths
            
            if r<0 or c<0 or r==ROW or c==COL or grid[r][c] != 0:
                return 0

            if r == ROW-1 and c == COL-1:
                numPaths += 1
                return 1

            grid[r][c] = 2

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            
            grid[r][c] = 0

            return numPaths

        ROW = len(grid)
        COL = len(grid[0])
        numPaths = 0

        return dfs(0,0)

