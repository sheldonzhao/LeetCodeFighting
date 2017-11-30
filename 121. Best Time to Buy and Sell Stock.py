class Solution:
    # TLE
    def maxProfit_TLE(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxValue = 0
        for i in range(1, len(prices)):
            num = prices[-i]
            validScope = prices[:len(prices) - i]
            if num - min(validScope) > 0:
                maxValue = max(maxValue, num - min(validScope))
        return maxValue

    def maxProfit(self, prices):
        """
        transfer the question to max subarray
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        dif_list = [prices[i + 1] - prices[i] for i in range(0, len(prices) - 1)]
        dp = [0]
        for i in range(1, len(dif_list) + 1):
            dp.append(dif_list[i - 1])
            if dp[i - 1] > 0:
                dp[-1] += dp[i - 1]
        return max(dp)


prices = [7, 1, 5, 3, 6, 4]
s = Solution()
res = s.maxProfit(prices)
print(res)
