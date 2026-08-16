class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l<=r:
            m = (l + r) // 2
            midval = nums[m]
            if midval == target:
                return m
            elif midval < target:
                l = m + 1
            else: 
                r = m - 1
        return l
