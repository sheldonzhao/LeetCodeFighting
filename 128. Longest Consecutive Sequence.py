'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''
'''
time: O(nlogn)
'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        nums = list(set(nums))
        if len(nums) == 1: return 1
        nums.sort()
        count = 1
        flag = 0
        max_length = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1 and flag == 0:
                count = 2
                flag = 1
            elif nums[i + 1] - nums[i] == 1 and flag == 1:
                count += 1
            else:
                max_length = max(max_length, count)
                count = 0
                flag = 0
        return max(max_length, count)


mySolution = Solution()
nums = [-6, -1, -1, 9, -8, -6, -6, 4, 4, -3, -8, -1]
re = mySolution.longestConsecutive(nums)
print(re)
