class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj =[[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        cycle, visit = set(), set()

        def dfs(crs):
            
            if crs in cycle:
                return False
            
            if crs in visit:
                return True

            cycle.add(crs)
            for nei in adj[crs]:
                if dfs(nei) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        
        return True