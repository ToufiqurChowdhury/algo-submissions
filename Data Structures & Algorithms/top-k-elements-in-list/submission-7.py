class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #bucket sort
        # TC: O(n)
        # numset = {}
        # freq = [[] for i in range(len(nums)+1)]

        # for n in nums:
        #     numset[n] = numset.get(n, 0) + 1

        # for n, c in numset.items():
        #     freq[c].append(n)
        
        # res = []
        # for i in range(len(freq)-1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)

        #         if len(res) == k:
        #             return res

        # return res

        # counter = {}
        # for n in nums:
        #     counter[n]=counter.get(n, 0) +1

        # heap = []
        # for item in counter.items():
        #     num, val = item
        #     heapq.heappush(heap, (val, num))

        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # res = [item[1] for item in heap]
        # return res 

        counts = Counter(nums)
        heap = [(-cnt, val) for val, cnt in counts.items()]
        heapq.heapify(heap)

        res = [heapq.heappop(heap)[1] for i in range(k)]
        print(res)
        return res
