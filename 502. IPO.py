'''
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital,
LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given several projects. For each project i, it has a pure profit Pi and a minimum capital of Ci is needed
to start the corresponding project. Initially, you have W capital.
When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

To sum up, pick a list of at most k distinct projects from given projects to maximize your final capital,
and output your final maximized capital.

You may assume all numbers in the input are non-negative integers.
The length of Profits array and Capital array will not exceed 50,000.
The answer is guaranteed to fit in a 32-bit signed integer.
'''


class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        k = min(len(Profits), k)
        used_capital = []
        while k != 0:
            capital_match = []
            max_profit = 0
            temp = 0
            for i in range(len(Capital)):
                if W >= Capital[i]:
                    capital_match.append(i)
            for i in capital_match:
                if Profits[i] >= max_profit and i not in used_capital:
                    temp = i
                    max_profit = Profits[i]
            W += max_profit
            used_capital.append(temp)
            k -= 1
        return W


mySolution = Solution()
K = 10
W = 0
Profits = [1, 2, 3]
Capital = [0, 1, 2]
re = mySolution.findMaximizedCapital(K, W, Profits, Capital)
print(re)
