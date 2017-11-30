'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
import time


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if nums is None or len(nums) == 0 or len(nums) == 1 or len(nums) == 2:
            return ans

        if len(nums) > 2:
            nums.sort()

        length = len(nums)
        for i in range(length - 2):
            sum2 = 0 - nums[i]
            for j in range(i + 1, length - 1):
                if sum2 - nums[j] in nums[j + 1:]:
                    h = nums.index(sum2 - nums[j], j + 1, length)
                    ans.append([nums[i], nums[j], nums[h]])

        '''
        ans_remove_duplicate = []
        for i in ans:
            if i not in ans_remove_duplicate:
                ans_remove_duplicate.append(i)
        '''

        #  optimization
        ans_remove_duplicate = set([tuple(i) for i in ans])
        r = [list(i) for i in ans_remove_duplicate]
        return r



nums1 = [7, -1, 14, -12, -8, 7, 2, -15, 8, 8, -8, -14, -4, -5, 7, 9, 11, -4, -15, -6, 1, -14, 4, 3, 10, -5, 2, 1, 6, 11,
         2, -2, -5, -7, -6, 2, -15, 11, -6, 8, -4, 2, 1, -1, 4, -6, -15, 1, 5, -15, 10, 14, 9, -8, -6, 4, -6, 11, 12,
         -15, 7, -1, -9, 9, -1, 0, -4, -1, -12, -2, 14, -9, 7, 0, -3, -4, 1, -2, 12, 14, -10, 0, 5, 14, -1, 14, 3, 8,
         10,
         -8, 8, -5, -2, 6, -11, 12, 13, -7, -12, 8, 6, -13, 14, -2, -5, -11, 1, 3, -6]
nums2 = [-1, 0, 1, 2, -1, -4]
solution = Solution()
start = time.time()
ans = solution.threeSum(nums1)
end = time.time()
print(len(ans))
print(end - start)
