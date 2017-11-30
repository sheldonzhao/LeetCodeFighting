'''
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''
'''
slide window
'''


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        count = 0
        index = 0
        queue = []
        save_min_len = []
        # establish window
        while count < s and index < len_nums:
            count += nums[index]
            queue.append(nums[index])
            index += 1
        if count < s:
            return 0
        # slide window
        while queue:
            while count >= s:
                value = queue.pop(0)
                count -= value
            save_min_len.append(len(queue) + 1)
            while count < s and index < len_nums:
                count += nums[index]
                queue.append(nums[index])
                index += 1
            if index == len_nums and count < s:
                return min(save_min_len)


mySolution = Solution()
nums = [2, 3, 1, 2, 4, 3]
s = 7
re = mySolution.minSubArrayLen(s, nums)
print(re)
