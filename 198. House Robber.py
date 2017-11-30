'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[1], nums[0] + nums[2])

        dp = [nums[0], nums[1], nums[0] + nums[2]]
        for i in range(3, len(nums)):
            if dp[i - 3] > dp[i - 2]:
                dp.append(nums[i] + dp[i - 3])
            else:
                dp.append(nums[i] + dp[i - 2])
        return max(dp[-1], dp[-2])


nums = [0]
s = Solution()
res = s.rob(nums)
print(res)
