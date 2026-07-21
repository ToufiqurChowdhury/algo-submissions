class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compmap = {}

        for i, n in enumerate(nums):
            comp = target-n
            if comp in compmap:
                return [compmap[comp], i]
            else:
                compmap[n] = i
        
        return None
        