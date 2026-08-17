import bisect

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        N = len(nums)

        for i in [0, N//2]:
            num = nums[i]
            start_index = bisect.bisect_left(nums, num) #log(N)
            print( N//2)
            if nums[start_index] == nums[N//2]:
                return num
        
        return -1
        