class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Greedy (BFS)

        [2, 3, 1, 1, 4]
        --- ----- -----
         0    1     2
        
        Time: O(n)

        """

        res = 0
        l = r = 0

        while r < len(nums)-1:

            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            
            l = r+1
            r = farthest
            res += 1
        
        return res




        
