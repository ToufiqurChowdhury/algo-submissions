class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res=[]

        def backtrack(i, sublist, total):
            if total == target:
                res.append(sublist.copy())
                return

            if i>= len(nums) or total > target:
                return

            sublist.append(nums[i])
            backtrack(i, sublist, total+nums[i])

            sublist.pop()
            backtrack(i+1, sublist, total)
            return 

        backtrack(0, [], 0)
        return res