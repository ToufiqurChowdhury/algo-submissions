class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) time | O(1) space 
        
        res = 0
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        
        while l < r:
            
            # move minimum pointer
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL-height[l]

            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR-height[r]
                
        return res