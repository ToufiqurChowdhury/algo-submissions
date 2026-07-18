class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        maxl = 0

        for n in numset:
            if n-1 not in numset:
                curr = n
                currlen = 1
                while curr+1 in numset:
                    curr += 1
                    currlen += 1
                
                maxl = max(maxl, currlen)
        
        return maxl