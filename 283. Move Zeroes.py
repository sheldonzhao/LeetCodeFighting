'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return
        count = 0
        while 0 in nums:
            nums.remove(0)
            count += 1
        for i in range(count):
            nums.append(0)

    def moveZeroes2(self, nums):
        if nums == []:
            return
        pos = 0
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
        for i in range(len(nums) - pos):
            nums[-i - 1] = 0
