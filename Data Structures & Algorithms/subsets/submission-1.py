class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # algo: backtrack
        # TC: O(n * 2^n)
        # SC: O(1)

        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # back track adding nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # back track without nums[i]
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res