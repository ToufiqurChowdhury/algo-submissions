class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # algo: backtrack
        # TC: O( n * 2^n)
        # SC: O(n)

        res, sol = [], []

        def backtrack(i):
            if i == len(nums):
                res.append(sol.copy())
                return

            # backtrack with num[i]
            sol.append(nums[i])
            backtrack(i+1)

            # backtrack without 
            sol.pop()
            backtrack(i+1)

        backtrack(0)
        return res
