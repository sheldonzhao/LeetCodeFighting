'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage
in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        flag, count, sum = 0, 0, 0
        for i in range(len(prices) - 1):
            if prices[i] <= prices[i + 1] and flag == 0:
                flag = 1
                count = prices[i + 1] - prices[i]
            elif prices[i] <= prices[i + 1] and flag == 1:
                count += prices[i + 1] - prices[i]
            else:
                sum += count
                count = 0
                flag = 0
        return sum+count
