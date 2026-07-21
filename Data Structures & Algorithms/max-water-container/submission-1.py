class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #ALGO: two pointer
        #TC: O(n)

        l, r = 0, len(heights)-1
        maxa = 0

        while l<r:
            area = (r-l) * min(heights[l], heights[r])
            maxa = max(maxa, area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r -= 1

        return maxa 
        