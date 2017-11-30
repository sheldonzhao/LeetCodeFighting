'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
The algorithm should run in linear time and in O(1) space.
'''
'''
蒙特卡罗算法
失败概率：(2/3)**15(很小的一个数了)
another solution: Majority Voting Algorithm
'''
import random


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        candidates = set([random.choice(nums) for i in range(15)])
        return [i for i in candidates if nums.count(i) > len(nums) // 3]


mySolution = Solution()
nums = [1]
re = mySolution.majorityElement(nums)
print(re)
