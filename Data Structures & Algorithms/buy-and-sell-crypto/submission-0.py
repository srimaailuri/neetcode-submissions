class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value=prices[-1]
        max_profit=0
        for i in range(len(prices)-2,-1,-1):
            max_profit=max(max_profit,max_value-prices[i])
            max_value=max(max_value,prices[i])
        return max_profit

