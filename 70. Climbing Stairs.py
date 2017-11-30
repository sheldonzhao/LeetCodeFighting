'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


class Solution(object):
    count = 0
    # TLE
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return
        if n == 1 or n == 2:
            self.count += 1

        self.climbStairs(n - 1)
        self.climbStairs(n - 2)
        return self.count

    def climbStarirs2(self, n):
        if n == 0:
            return 0
        dp = [0]
        for i in range(1, n + 1):
            if i == 1:
                dp.append(1)
            elif i == 2:
                dp.append(dp[1] + 1)
            else:
                dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1]


s = Solution()
res = s.climbStarirs2(3)
print(res)
