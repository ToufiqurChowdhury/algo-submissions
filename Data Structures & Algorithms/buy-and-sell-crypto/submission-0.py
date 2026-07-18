class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Two pointer init to check the max profit
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            #check if sell makes profit
            if prices[l] < prices[r]: 
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r

            r += 1
        
        return maxProfit
            
        