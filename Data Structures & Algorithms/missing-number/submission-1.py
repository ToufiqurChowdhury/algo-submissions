class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        ans = 0
        for n in range(1, n+1):
            ans ^= n
        
        for num in nums:
            ans ^= num

        return ans
        

        """
        res = len(nums)

        for i in range(len(nums)):
            res += (i-nums[i])
        
        return res
        """