class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        maxl = 0

        # check for n in numset
        for n in numset:
            # prev check
            if n-1 not in numset:
                curr = n
                currlen = 1

                #next num check
                while curr+1 in numset:
                    curr += 1
                    currlen += 1
                
                # find max
                maxl = max(maxl, currlen)
        
        return maxl