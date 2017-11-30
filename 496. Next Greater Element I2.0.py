'''
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements
are subset of nums2. Find all the next greater numbers for nums1's elements
in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its
right in nums2. If it does not exist, output -1 for this number.
'''
'''
time: O(n)
space O(n)
'''


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        hash_map = {}
        for i in nums:
            while len(stack) and stack[-1] < i:
                hash_map[stack.pop()] = i
            stack.append(i)
        res = [-1] * len(findNums)
        for i in range(len(findNums)):
            if findNums[i] in hash_map:
                res[i] = hash_map[findNums[i]]
        return res


mySolution = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
re = mySolution.nextGreaterElement(nums1, nums2)
print(re)
