class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Check Union Find also for another solution

        # O(e+v) time and space

        # 1. Build graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # DFS on node
        def dfs(node):
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        seen = set()
        ans = 0

        # 2. iterate over nodes
        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)
                #print("Node:", i)

        return ans