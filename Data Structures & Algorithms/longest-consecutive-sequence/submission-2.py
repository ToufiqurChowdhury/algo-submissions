class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxl = 0

        for n in numset:
            if n-1 not in numset:
                cur = n
                curlen = 1

                while cur+1 in numset:
                    cur += 1
                    curlen += 1
                
                maxl = max(maxl, curlen)

        return maxl    