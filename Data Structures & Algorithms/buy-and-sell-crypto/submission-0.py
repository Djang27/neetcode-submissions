class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 1:
            return 0
            
        lowestPrice = prices[0]
        highProfit = 0

        for num in range(len(prices)):
            if prices[num] < lowestPrice:
                lowestPrice = prices[num]
            profit = prices[num] - lowestPrice
            if profit > highProfit:
                highProfit = profit
            
        return highProfit 

