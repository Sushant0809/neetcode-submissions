class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini = max(prices)
        profit = 0

        for price in prices:

            mini = min(price,mini)
            profit = max(profit, price-mini)
            print(mini, profit)
        
        return profit

        