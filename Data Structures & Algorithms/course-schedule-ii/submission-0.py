class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prerecs = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            prerecs[crs].append(pre)
        
        res = []
        cycle, visit = set(), set()

        def dfs(crs):

            if crs in cycle:
                return False

            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prerecs[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return res
