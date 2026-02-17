class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest_price = 100000
        profit = 0

        for price in prices:
            if price < lowest_price:
                lowest_price = price
            if price - lowest_price > profit:
                profit = price - lowest_price
        
        return profit