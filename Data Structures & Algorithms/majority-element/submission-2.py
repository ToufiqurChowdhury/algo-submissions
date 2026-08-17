import bisect

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) // 2

        candidate = nums[n]

        left = bisect.bisect_left(nums, candidate)
        right = bisect.bisect_right(nums, candidate)

        if right - left > n:
            return candidate

        return -1
        