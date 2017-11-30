'''
Given a list of non-negative numbers and a target value k,
write a function to check if the array has a continuous subarray of size at least 2 that sums up
to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
'''


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        len_nums = len(nums)
        if len_nums < 2: return False
        if k == 0:
            for i in range(len_nums - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False
        for i in range(len_nums):
            sum_value = nums[i]
            for j in range(i+1, len_nums):
                sum_value += nums[j]
                if sum_value % k == 0:
                    return True
        return False


mySolution = Solution()
nums = [0]
nums1 = [23, 2, 4, 6, 7]
k2 = -6
k = 0
k1 = -1
re = mySolution.checkSubarraySum(nums, k1)
print(re)
