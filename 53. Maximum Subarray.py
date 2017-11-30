'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp.append(nums[i] + dp[i - 1])
            else:
                dp.append(nums[i])
        return max(dp)


s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
res = s.maxSubArray(nums)
print(res)
