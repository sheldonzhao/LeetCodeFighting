'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1
'''
'''
看似复杂的问题通过对子结构的加法和的利用得到答案
'''


class Solution(object):
    def __init__(self):
        self.max = 0

    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        hash_map = {0: [-1]}
        nums_sum = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        for pos in range(len(nums)):
            nums_sum += nums[pos]
            if nums_sum not in hash_map:
                hash_map[nums_sum] = [pos]
            else:
                hash_map[nums_sum].append(pos)
        max_value = 0
        for value in hash_map.values():
            max_value = max(max_value, value[-1] - value[0])
        return max_value


mySolution = Solution()
nums = [0, 0, 1, 0, 0, 0, 1, 1]
re = mySolution.findMaxLength(nums)
print(re)
