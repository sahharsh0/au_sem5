#array given prices where prices[i] is the price of a given stock on the ith day
# you want to maximize your profit by choosing a single day to buy one stock and choosing a different day to sell the stock
#return max profit you can achieve from this transaction. If you cannot achieve any profit, return 0
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit
print('Current max profit:', Solution().maxProfit([7,1,5,3,6,4]))