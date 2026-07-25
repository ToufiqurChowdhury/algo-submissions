class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        
        def dfs(r, c):

            if r<0 or c<0 or r==rows or c==cols or grid[r][c] != 1:
                return 0
            
            grid[r][c] = -1

            area = 1
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)

            return area
        
        
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    size = dfs(r, c)
                    maxArea = max(maxArea, size)
        
        return maxArea