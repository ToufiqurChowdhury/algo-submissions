class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):            
            if r<0 or c<0 or r==ROW or c==COL or grid[r][c] != 0 or (r,c) in visit:
                return 0

            if r == ROW-1 and c == COL-1:
                return 1
            visit.add((r,c))

            count = 0
            count += dfs(r+1, c)
            count += dfs(r-1, c)
            count += dfs(r, c+1)
            count += dfs(r, c-1)

            visit.remove((r,c))
            return count

        ROW = len(grid)
        COL = len(grid[0])
        visit = set()

        return dfs(0,0)

