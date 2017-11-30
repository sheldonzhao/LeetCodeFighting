'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
'''
'''
simple solution : use hashmap
learning point: if i not in HashMap: is much more efficient than if i not in List:
'''

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        ans = []
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                ans.append(i)
        return ans


mySolution = Solution()
nums = [1, 2, 3, 3, 4, 4]
re = mySolution.findDuplicates(nums)
print(re)
