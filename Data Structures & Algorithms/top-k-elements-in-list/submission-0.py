class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Algo: conver nums in key value dictionary/hashmap using Counter (frequency)
        # Use heap to find top k items
        # O(n) time | O(n) space

        counts = Counter(nums)

        heap = []

        for item in counts.items():
            key, val = item
            heapq.heappush(heap, (val, key))

            if len(heap) > k:
                heapq.heappop(heap)
            
        res = [pair[1] for pair in heap]

        return res
        