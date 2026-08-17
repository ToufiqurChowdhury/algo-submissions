class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) // 2

        for i in range(len(nums)):
            num = nums[i]
            
            # We can use the property that in a sorted array, the 
            # majority element must occupy the middle index (n // 2).
            if nums[n] == num:
                return nums[n]
        return nums[n]
        