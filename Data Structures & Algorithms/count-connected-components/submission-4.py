class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        
        def dfs(node):
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        
        seen = set()
        ans = 0

        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)

        return ans