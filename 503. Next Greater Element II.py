'''
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array,
which means you could search circularly to find its next greater number.
If it doesn't exist, output -1 for this number.
'''
'''
Two methods:
1. double the nums to simplify the operation of circular
Time: O(n**2)
Space: O(n)
2. use a stack to facilitate the look up
Time: O(n)
Space: O(n)
'''


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        len_nums = len(nums)
        ans = [-1] * len_nums
        s = nums[::-1]
        for i in range(len_nums):
            num = nums[-i - 1]
            while s and s[-1] <= num:
                s.pop()
            if s:
                ans[-i - 1] = s[-1]
            s.append(num)
        return ans


mySolution = Solution()
nums = [1, 2, 1]
re = mySolution.nextGreaterElements(nums)
print(re)
