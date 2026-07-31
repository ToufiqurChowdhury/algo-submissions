class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        res = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            heapq.heappush(minheap, [dist, x, y])  
            
        for i in range(k):
            _, m, n = heapq.heappop(minheap)
            res.append([m,n])
        
        return res